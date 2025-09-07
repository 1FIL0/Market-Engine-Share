import subprocess
import os
import signal
import threading
import sys
from typing import IO, Callable, Optional, Union
from subprocess import Popen
import logger

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
        )
    else:
        proc = Popen(
            command,
            stdout=stdout,
            bufsize=1,
            text=True,
            preexec_fn=os.setsid,
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
        
    if sys.platform == "win32":
        proc.send_signal(signal.CTRL_BREAK_EVENT)
    else:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    logger.sendMessage(f"Killed {proc}")