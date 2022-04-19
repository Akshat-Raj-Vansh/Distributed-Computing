import marshal
import socket
import json
import _thread
import sys
import time
import random
import os
from xmlrpc.client import Marshaller
import tqdm
import threading
import os
import subprocess
import _thread
from add import Add

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

    def marshalling(self, obj):
        # data = {}
        # data["num1"]=obj.num1
        # data["num2"]=obj.num2
        # print(data)
        data = obj.getJson()
        print(data)
        return marshal.dumps(data)
    
    def demarshalling(self, bytes):
        data = marshal.loads(bytes)
        print(data)
        res  = Add(int(data["num1"]), int(data["num2"], int(data["sum"])))
        # res = Add.fromJson(data)
        return res
    

    def listen(self, client):
        while True:
            data = client.recv(BUFFER_SIZE)
            obj = self.demarshalling(data)
            print(obj.getSum())


    def send(self, client):
        while True:
            message = input("")
            if(message[:message.find("(")] == "ADD"):
                self.nums = message[message.find("(")+1:message.find(")")].split(',')
                add = Add(int(self.nums[0]), int(self.nums[1]), 0)
                client.send(self.marshalling(add))


    def start(self):
        client = self.createSocket(self.port)
        _thread.start_new_thread(self.send, (client,))
        _thread.start_new_thread(self.listen, (client,))
        while True:
            continue


if __name__ == '__main__':
    client = Client('192.168.26.196', 1237)
    client.start()
