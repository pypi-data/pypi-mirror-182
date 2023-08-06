from __future__ import annotations
import os

class CLog:
    def __init__(self, path: str = os.getcwd()) -> None:
        self.__path = path
        self.fpath = f'{self.__path}/Changelog.clog'
        if not os.path.exists(self.fpath):
            f = open(self.fpath, 'w')
            f.write("Changelog\n\n")
            f.close()
    
    def WriteLog(self, new_data: LogData) -> None:
        f = open(self.fpath, 'a')
        for item in new_data.data:
            f.write(f'{item}\n')
        f.write('\n')
        f.close()

 
class LogData:
    version = ""
    data = []
    def __init__(self, version: str, contributor: str) -> None:
        self.data.append(f'Version {version} - Edited by: {contributor}')
        self.version = version

    def AddEntry(self, change: str) -> None:
        self.data.append(f'- {change}')
        

def GetExistingLog(path: str):
    return CLog(path)

def DeleteLog(path):
    os.remove(f'{path}/Changelog.clog')