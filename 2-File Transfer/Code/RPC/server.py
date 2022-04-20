import socket as socket
import _thread
import threading
import random
import os
import tqdm
from time import sleep
import time
from client import Client

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

    def decode(self, value):
        return value.decode('ascii')

    def encode(self, value):
        return value.encode('ascii')

    def add(self, nums):
        return sum(nums)
    
    def listen(self, client, client_addr):
        while True:
            data = client.recv(BUFFER_SIZE)
            data = self.decode(data)
            print(data)
            message = data[:data.find('(')]
            if message == "ADD":
                nums = data[data.find('(')+1:data.find(')')].split(',')
                # sum  = int(nums[0]) + int(nums[1])
                nums = [int(x) for x in nums]
                sum = self.add(nums)
                client.send(self.encode("RESULT({})".format(sum)))

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
    server = Server(1237, host="127.0.0.1")
    server.start()
