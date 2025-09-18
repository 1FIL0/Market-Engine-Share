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