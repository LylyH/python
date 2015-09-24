#!/usr/bin/python3
# coding: utf-8
 
import socket
import threading

class Server():

    def __init__(self):
        tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpsock.bind(("10.41.176.208",1234))

        while True:
            tcpsock.listen(10)
            print( "En écoute...")
            (clientsocket, (ip, port)) = tcpsock.accept()
            newthread = ClientThread(ip, port, clientsocket)
            newthread.start()


class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print(" ---- Nouveau thread | IP : %s - PORT : %s" % (self.ip, self.port))

    def run(self): 
   
        print("Connection de %s %s" % (self.ip, self.port))

        r = self.clientsocket.recv(2048)
        print("Text : " + r.decode() + "...")
        print("Client déconnecté...")

if __name__ == '__main__':
	Server = Server()