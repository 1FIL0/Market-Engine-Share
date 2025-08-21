import subprocess
import os
import signal
import threading
from typing import Callable, Optional
from subprocess import Popen

def runSubProcess(command: list[str], exitCallback: Optional[Callable[[Popen[str]], None]]=None):
    proc: Popen[str] = Popen(command, stdout=subprocess.PIPE, preexec_fn=os.setsid, bufsize=1, universal_newlines=True)
    print("Started " + str(proc))
    if exitCallback:
        def waitAndCallback():
            proc.wait()
            exitCallback(proc)
        threading.Thread(target=waitAndCallback, daemon=True).start()
    return proc

def killSubProcess(proc: Popen[str]):
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    print("killed " + str(proc))
    