from datetime import datetime

class Config:
    def __init__(self):
        self._urls = []
        self._number = int
        self._pathsafe = str
        self._datetime = datetime.now().strftime('%Y%m%d')
        self._config = r'./config.txt'
    

    def load_config(self):
        with open(self._config, "r") as file:
            for line in file.readlines():
                if "number=" in line:
                    self._number = int(line.split("=")[1].strip())
                elif "pathsafe=" in line:
                    self._pathsafe = line.split("=")[1].strip()
                elif "date=" in line:
                    if int(self._datetime) > int(line.split("=")[1]):
                        self._number = 0


    def write_config(self):
        with open(self._config, "w") as file:
            file.write(f"number={self._number}\n")
            file.write(f"pathsafe={self._pathsafe}\n")
            file.write(f"date={self._datetime}\n")

