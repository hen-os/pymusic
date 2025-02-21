import sys
import conversor
from config import Config
from datetime import datetime

class App(Config):
    def __init__(self):
        self.functions = {
                'l': [self.load_urls],
                'h': [self.help, 'help'],
                'q': [self.exit_program, 'exit']
        }
    

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
        print('     Simple program to conversor files    \n')
        print('\n h to help \n')

        while True:
            self.command()

if __name__ == "__main__":
    con = Conversor()
    con.load_config()
    con.load_urls("./link.txt")
    con.conversorMP3()
    con.write_config()
