from typing import Optional
from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import requests
import user_auth

class QTRequestWorker(QObject):
    finishedSuccess = pyqtSignal(object)
    finishedError = pyqtSignal(object)

    def __init__(self, url: str, sleepMin: float, parent: Optional[QObject]=None):
        super().__init__(parent)
        self.url = url
        self.sleepMin = sleepMin
        self.running = False

        self.timer = QTimer()
        self.timer.setInterval(int(self.sleepMin * 60 * 1000))
        self.timer.timeout.connect(self.makeRequest)

    def start(self):
        self.running = True
        self.makeRequest()
        self.timer.start()

    def stop(self):
        self.running = False
        self.timer.stop()

    def makeRequest(self):
        if not self.running:
            return
        try:
            token = user_auth.getKeyringToken()
            response = requests.post(self.url, json={"token": token})
            if response.status_code != 200:
                self.finishedError.emit(response.json())
            else:
                self.finishedSuccess.emit(response.json())
        except Exception as e:
            self.finishedError.emit({"error": str(e)})