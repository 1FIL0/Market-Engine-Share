from typing import Optional
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

class QTTimeoutWorker(QObject):
    timeout = pyqtSignal()

    def __init__(self, sleepSec: float, parent: Optional[QObject]=None):
        super().__init__(parent)
        self.sleepSec = sleepSec
        self.timer = QTimer()
        self.timer.setInterval(int(self.sleepSec * 1000))
        self.timer.timeout.connect(self.timeout)

    def start(self):
        self.timer.start()

    def stop(self):
        self.timer.stop()