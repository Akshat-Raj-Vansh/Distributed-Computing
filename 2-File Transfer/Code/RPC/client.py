import socket
import json
import _thread
import time
import random
import os
import tqdm
import threading
import os
import subprocess
import _thread

BUFFER_SIZE = 5120
SEPARATOR = "<SEPARATOR>"


class Error:
    commandInputError = Exception("Please enter correct command")
    portInputError = Exception("Please enter correct port number")
    controllerError = Exception("Controller Error. Try After Sometime")
    createRoomError = Exception("Error in creating the room")


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connections = []

    def createSocket(self, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.host, port))
        return client

    def decode(self, value):
        return value.decode('ascii')

    def encode(self, value):
        return value.encode('ascii')

    def listen(self, client):
        while True:
            data = client.recv(BUFFER_SIZE)
            data = self.decode(data)
            print(data)
            message = data[:data.find('(')]
            if(message == "ADD"):
                nums = data[data.find('(')+1:data.find(')')].split(',')
                print(nums)
                self.send_command(nums, client)


    def send(self, client):
        while True:
            message = input("")
            if(message[:message.find("(")] == "ADD"):
                self.fileName = message[message.find("(")+1:message.find(")")]
                client.send(self.encode(message))


    def start(self):
        client = self.createSocket(self.port)
        _thread.start_new_thread(self.send, (client,))
        _thread.start_new_thread(self.listen, (client,))
        while True:
            continue


if __name__ == '__main__':
    client = Client('192.168.26.196', 1237)
    client.start()
