import socket
import json

IP = '127.0.0.1'
port = 8000
addr = (IP, port)
DISCONNECT = "quit"             #keyword for leaving the server
SHUTDOWN = "SHUT DOWN"          #keyword for shutting down server

#opcommands:
#1 = login
#2 = sending message

header = {'username': '', 'message': '','length': '', 'command': ''}    #dictionary that will be sent to server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                 #this socket is using udp




def login():
        print("Enter username:", end = ' ')     
        user = input()
        header['command'] = 1
        header['username'] = user
        header['message'] = user
        header['length'] = len(user)
        print('logged in')
        send = json.dumps(header).encode('utf-8')       #turns header to bytes before sending
        sock.sendto(send, addr)
        
def sendMsg():
        connected = True

        while connected:
                print('Enter message:', end = ' ')
                msg = input()
                size = len(msg)

                if (msg == DISCONNECT or msg == SHUTDOWN):      #disconnect or shutdown server
                        connected = False
                header['command'] = 2
                header['message'] = msg
                header['length'] = size
                send = json.dumps(header).encode('utf-8')       #disctionary is turned into bytes and sent to the server
                sock.sendto(send, addr)
                print("sent")
        
        sock.close                                              #close socket

login()
sendMsg()