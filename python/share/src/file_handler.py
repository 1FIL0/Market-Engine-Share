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

import json
import os
import tempfile
import shutil
from typing import Any
import definitions
from filelock import FileLock

def makeDir(dirPath: str):
    os.makedirs(dirPath, exist_ok=True)

def writeFile(filePath: str, data: Any, binary: bool = False):
    flags = "w"
    if binary: flags = "wb"
    with open(filePath, flags) as f:
        _ = f.write(data)
        f.close()

def copyFile(fromPath: str, toPath: str):
    _ = shutil.copy(fromPath, toPath)

def clearJsonFile(filePath: str):
    with open(filePath, 'w') as file:
        data = {}
        json.dump(data, file, indent=4)
        file.close()

def replaceJsonDataAtomic(filePath: str, newData: dict[str, Any], lockTimeout: int = 10):
    lockPath = filePath + ".lock"
    lock = FileLock(lockPath, timeout=lockTimeout)
    
    with lock:
        writeTempReplace(filePath, newData)

def writeTempReplace(filePath: str, newData: dict[str, Any]):
    dirName = os.path.dirname(filePath) or "."
    fd, tmpPath = tempfile.mkstemp(dir=dirName)
    try:
        with os.fdopen(fd, "w") as tmpFile:
            json.dump(newData, tmpFile, indent=4)
            tmpFile.flush()
            os.fsync(tmpFile.fileno())
        os.replace(tmpPath, filePath)
    except Exception:
        os.remove(tmpPath)

def clearJsonFileArray(filePath: str):
    with open(filePath, 'w') as file:
        data: dict[str, Any] = {"DATA": []}
        json.dump(data, file, indent=4)
        file.close()

def appendJsonDataArray(filePath: str, appendedData: Any):
    newData = {}
    with open(filePath, 'r') as readFile:
        newData = json.load(readFile)
        newData["DATA"].append(appendedData)
    with open(filePath, 'w') as writeFile:
        json.dump(newData, writeFile, indent=4)
        _ = writeFile.write("\n")
    readFile.close()
    writeFile.close()

def readFileLocked(filePath: str, binary: bool = False, lockTimeout: int = 10):
    lockPath = filePath + ".lock"
    lock = FileLock(lockPath, timeout=lockTimeout)

    flags = "rb" if binary else "r"
    encoding = None if binary else "utf-8"

    with lock:
        with open(filePath, flags, encoding=encoding) as f:
            return f.read()

def loadJson(filePath: str) -> dict[Any, Any]:
    data: str = readFileLocked(filePath)
    jsonData: dict[Any, Any] = json.loads(data)
    return jsonData
    
    