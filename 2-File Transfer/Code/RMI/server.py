import json
import marshal
import socket as socket
import _thread
import sys
import threading
import random
import os
import tqdm
from time import sleep
import time
from client import Client
from add import Add

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 5


class Server:
    def __init__(self, port, host=""):
        self.host = host
        self.port = port
        self.connection = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def configure(self):
        try:
            self.server.bind((self.host, self.port))
            print("Server binded to port", self.port)
            self.server.listen(5)
            print("Server is listening")
        except Exception as e:
            print(e)

  
    def marshalling(self, obj):
        data = obj.getJson()
        print(data)
        return marshal.dumps(data)
    
    def demarshalling(self, bytes):
        data = marshal.loads(bytes)
        print(data)
        res  = Add(int(data["num1"]), int(data["num2"]), 0)
        return res

    def listen(self, client, client_addr):
        while True:
            data = client.recv(BUFFER_SIZE)
            obj = self.demarshalling(data)
            obj.findSum()
            client.send(self.marshalling(obj))

    def threaded(self, client, client_addr):
        _thread.start_new_thread(self.listen, (client, client_addr))
        while True:
            continue

    def start(self):
        self.configure()
        while True:
            client, client_addr = self.server.accept()
            print('Connected to :', client_addr[0], ':', client_addr[1])
            _thread.start_new_thread(
                self.threaded, (client, client_addr[1]))


if __name__ == '__main__':
    server = Server(1237, host="192.168.26.196")
    server.start()
