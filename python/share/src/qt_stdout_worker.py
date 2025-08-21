from typing import Optional
from PyQt5.QtCore import QThread, pyqtSignal
import select
import time
from subprocess import Popen

class QTStdoutWorker(QThread):
    lineRead = pyqtSignal(str)

    def __init__(self, proc: Popen[str], parent:Optional[QThread]=None):
        super().__init__(parent)
        self.proc = proc
        self.running = True

    def run(self):
        buffer: list[str] = []
        last_emit = time.time()
        while self.running:
            # Non-blocking check for new lines
            rlist, _, _ = select.select([self.proc.stdout], [], [], 0.1)
            if rlist and self.proc.stdout:
                line = self.proc.stdout.readline()
                if line:
                    buffer.append(line.rstrip())

            now = time.time()
            if buffer and (now - last_emit > 0.1 or len(buffer) > 20):
                self.lineRead.emit('\n'.join(buffer))
                buffer.clear()
                last_emit = now

    def stop(self):
        self.running = False