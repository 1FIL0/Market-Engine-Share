#* Market Engine Share
#* Copyright (C) 2025 OneFil (1FIL0) https://github.com/1FIL0
#*
#* This program is free software: you can redistribute it and/or modify
#* it under the terms of the GNU General Public License as published by
#* the Free Software Foundation, either version 3 of the License, or
#* (at your option) any later version.
#*
#* This program is distributed in the hope that it will be useful,
#* but WITHOUT ANY WARRANTY; without even the implied warranty of
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#* GNU General Public License for more details.
#*
#* You should have received a copy of the GNU General Public License
#* along with this program.  If not, see <http://www.gnu.org/licenses/>.
#* See LICENCE file.

import subprocess
import threading
import sys
from typing import IO, Callable, Optional, Union
from subprocess import Popen
import logger
import psutil
import signal
import ctypes
import ctypes.wintypes

# FUCK WINDOWS

def runSubProcess(
    command: list[str],
    exitCallback: Optional[Callable[[Popen[str]], None]] = None,
    stdout: Union[int, IO[str], None] = subprocess.PIPE,
) -> Popen[str]:

    proc = None
    
    if sys.platform == "win32":
        kernel32 = ctypes.windll.kernel32

        # Define missing types
        SIZE_T = ctypes.c_size_t
        ULONG_PTR = ctypes.c_size_t  # pointer-sized unsigned long

        class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("PerProcessUserTimeLimit", ctypes.wintypes.LARGE_INTEGER),
                ("PerJobUserTimeLimit", ctypes.wintypes.LARGE_INTEGER),
                ("LimitFlags", ctypes.wintypes.DWORD),
                ("MinimumWorkingSetSize", SIZE_T),
                ("MaximumWorkingSetSize", SIZE_T),
                ("ActiveProcessLimit", ctypes.wintypes.DWORD),
                ("Affinity", ULONG_PTR),
                ("PriorityClass", ctypes.wintypes.DWORD),
                ("SchedulingClass", ctypes.wintypes.DWORD),
            ]

        class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
                ("IoInfo", ctypes.c_byte * 48),
                ("ProcessMemoryLimit", SIZE_T),
                ("JobMemoryLimit", SIZE_T),
                ("PeakProcessMemoryUsed", SIZE_T),
                ("PeakJobMemoryUsed", SIZE_T),
            ]

        JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000

        job = kernel32.CreateJobObjectW(None, None)
        info = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
        info.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        kernel32.SetInformationJobObject(job, 9, ctypes.byref(info), ctypes.sizeof(info))

        proc: Popen[str] = Popen(
            command,
            stdout=stdout,
            bufsize=1,
            text=True,
            encoding="utf-8"
        )
        kernel32.AssignProcessToJobObject(job, proc._handle)
    else:
        import prctl
        proc = Popen(
            command,
            stdout=stdout,
            bufsize=1,
            text=True,
            preexec_fn=lambda: prctl.set_pdeathsig(signal.SIGTERM),
            encoding="utf-8"
        )

    logger.sendMessage(f"Started process {proc.pid}: {command}")

    if exitCallback:
        def waitAndCallback() -> None:
            proc.wait()
            exitCallback(proc)

        threading.Thread(target=waitAndCallback, daemon=True).start()

    return proc

def killSubProcess(proc: Popen[str]):
    if proc.poll() is not None:
        return

    try:
        parent = psutil.Process(proc.pid)
    except psutil.NoSuchProcess:
        return

    # KILL CHILDREN
    for child in parent.children(recursive=True):
        try:
            child.kill()
        except psutil.NoSuchProcess:
            pass

    # KILL PARENT
    try:
        parent.kill()
    except psutil.NoSuchProcess:
        pass

    parent.wait()

    logger.sendMessage(f"Killed process {proc.pid}")

