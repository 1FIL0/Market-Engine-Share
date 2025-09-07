import os
import time
from typing import Callable, Optional
from PyQt5.QtCore import QObject, pyqtSignal, QTimer

class QTFWatcherWorker(QObject):
    refreshed = pyqtSignal()

    def __init__(self, filePath: str, sleepSec: float, refreshIntervalSec: float, refreshFunction: Callable[[], None], parent: Optional[QObject]=None):
        super().__init__(parent)
        self.filePath = filePath
        self.sleepSec = sleepSec
        self.refreshIntervalSec = refreshIntervalSec
        self.refreshFunction = refreshFunction
        self.lastMTime = 0
        self.startIntervalTime = time.time()
        self.running = False

        self.timer = QTimer()
        self.timer.setInterval(int(self.sleepSec * 1000)) # ms
        self.timer.timeout.connect(self.checkFile)

    def start(self):
        self.running = True
        self.timer.start()

    def stop(self):
        self.running = False
        self.timer.stop()

    def checkFile(self):
        if not self.running:
            return

        if self.startIntervalTime + self.refreshIntervalSec > time.time():
            return

        self.startIntervalTime = time.time()

        if self.fileMTimeNewer():
            self.callRefreshFunction()
            self.syncMTime()

    def fileMTimeNewer(self):
        try:
            mtime = os.path.getmtime(self.filePath)
            if mtime > self.lastMTime:
                return True
        except FileNotFoundError:
            return False

    def syncMTime(self):
        self.lastMTime = os.path.getmtime(self.filePath)

    def callRefreshFunction(self):
        self.refreshFunction()
        self.refreshed.emit()