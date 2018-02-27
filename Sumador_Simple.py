#!/usr/bin/python3

import socket
import random
import calculadora


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((socket.gethostbyname('localhost'), 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        request = str(recvSocket.recv(2084),'utf-8')
        print(request)
        resource = request.split()[1]
        print(resource)
        _,op1,oper,op2 = resource.split('/')
        num1 = int(op1)
        num2 = int(op2)
        html_answer = calculadora.funciones[oper] (num1,num2)
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        '<html><title>SumadorSimple</title>' +
						str(html_answer)+
                        '\r\n', 'utf-8'))
        recvSocket.close()
        
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()