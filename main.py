import sys
import conversor
from datetime import datetime

class App:
    def __init__(self):
        self._urls = []
        self._number = int
        self._pathsafe = str
        self._datetime = datetime.now().strftime('%Y%m%d')
        self._config = r'./config.txt'
        
        self.functions = {
                'l': [self.load_urls],
                'h': [self.help, 'help'],
                'q': [self.exit_program, 'exit']
            }


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


    def load_urls(self, path):
        with open(path, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                self._urls.append(line)


    def help(self):
        for key, value in self.functions.items():
            print(f'{key} : {value[1]}')


    def exit_program(self):
        if input("Do you want to exit? (y/n): ").lower() == 'y':
            sys.exit(0)


    def command(self):
        select = input('$_> ')
        self.functions[select][0]()


    def main(self):
        print('     Simple program to download in old format mp3    \n')
        print('\n h to help \n')

        while True:
            self.command()
