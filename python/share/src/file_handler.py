import json
import os
import tempfile
import shutil
from typing import Any
import definitions

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

def replaceJsonDataAtomic(filePath: str, newData: dict[str, any], retries: int = 5, delay: float = 0.05):
    dirName = os.path.dirname(filePath)
    fd, tmpPath = tempfile.mkstemp(dir=dirName)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as tmpFile:
            json.dump(newData, tmpFile, indent=4)
            tmpFile.flush()
            os.fsync(tmpFile.fileno())

        if definitions.SYSTEM == definitions.SYSTEM_WINDOWS:
            for attempt in range(retries):
                try:
                    os.replace(tmpPath, filePath)
                    break
                except PermissionError:
                    time.sleep(delay)
            else:
                raise RuntimeError(f"Failed to replace {filePath} after {retries} attempts")
        elif definitions.SYSTEM == definitions.SYSTEM_LINUX:
            os.replace(tmpPath, filePath)
    finally:
        if os.path.exists(tmpPath):
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
    
    