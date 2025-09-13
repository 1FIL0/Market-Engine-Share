import subprocess
import os
import threading
import sys
from typing import IO, Callable, Optional, Union
from subprocess import Popen
import logger
import psutil

def runSubProcess(
    command: list[str],
    exitCallback: Optional[Callable[[Popen[str]], None]] = None,
    stdout: Union[int, IO[str], None] = subprocess.PIPE,
) -> Popen[str]:
    if sys.platform == "win32":
        proc: Popen[str] = Popen(
            command,
            stdout=stdout,
            bufsize=1,
            text=True,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
            encoding="utf-8"
        )
    else:
        proc = Popen(
            command,
            stdout=stdout,
            bufsize=1,
            text=True,
            preexec_fn=os.setsid,
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
