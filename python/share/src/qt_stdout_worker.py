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
from PyQt5.QtCore import QThread, pyqtSignal
import select
import time
from subprocess import Popen

class QTStdoutWorker(QThread):
    lineRead = pyqtSignal(str)

    def __init__(self, proc: Popen[str], parent: Optional[QThread]=None):
        super().__init__(parent)
        self.proc = proc
        self.running = True

    def run(self):
        buffer: list[str] = []
        lastEmit = time.time()
        while self.running and self.proc.stdout:
            line = self.proc.stdout.readline()
            if not line:  # EOF
                if buffer:
                    self.lineRead.emit('\n'.join(buffer))
                break
            buffer.append(line.rstrip())
    
            now = time.time()
            if buffer and (now - lastEmit > 0.1 or len(buffer) > 20):
                self.lineRead.emit('\n'.join(buffer))
                buffer.clear()
                lastEmit = now

    def stop(self):
        self.running = False