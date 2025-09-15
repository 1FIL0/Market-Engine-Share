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
        raise

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

def readFile(filePath: str, binary: bool = False):
    flags = 'r'
    if binary: flags = 'rb'
    encoding = None if binary else "utf-8"
    with open(filePath, flags, encoding=encoding) as f:
        data = f.read()
        f.close()
        return data

def loadJson(filePath: str) -> dict[Any, Any]:
    data: str = readFile(filePath)
    jsonData: dict[Any, Any] = json.loads(data)
    return jsonData
    
    