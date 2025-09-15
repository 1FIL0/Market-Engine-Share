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
    
        class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("PerProcessUserTimeLimit", ctypes.wintypes.LARGE_INTEGER),
                ("PerJobUserTimeLimit", ctypes.wintypes.LARGE_INTEGER),
                ("LimitFlags", ctypes.wintypes.DWORD),
                ("MinimumWorkingSetSize", ctypes.wintypes.SIZE_T),
                ("MaximumWorkingSetSize", ctypes.wintypes.SIZE_T),
                ("ActiveProcessLimit", ctypes.wintypes.DWORD),
                ("Affinity", ctypes.wintypes.ULONG_PTR),
                ("PriorityClass", ctypes.wintypes.DWORD),
                ("SchedulingClass", ctypes.wintypes.DWORD),
            ]
    
        class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
            _fields_ = [
                ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
                ("IoInfo", ctypes.c_byte * 48),
                ("ProcessMemoryLimit", ctypes.wintypes.SIZE_T),
                ("JobMemoryLimit", ctypes.wintypes.SIZE_T),
                ("PeakProcessMemoryUsed", ctypes.wintypes.SIZE_T),
                ("PeakJobMemoryUsed", ctypes.wintypes.SIZE_T),
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

