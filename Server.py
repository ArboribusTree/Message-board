import socket
import json
 
IP = '127.0.0.1'                                                #this ip is the ip to talk to self
port = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)         #this socket is using udp
DISCONNECT = 'quit'
 
addr = sock.bind((IP, port))            
users = []

print(f"Listening from port {port}")            #f string format. dont worry just printing

def login(users, username):                     #method for accepting usernames. users is a list of usernames. prints users
        users.append(username)
        print(users)

def logout(users, username):                    #method for logging out. removes user from list. prints users
        users.remove(username)
        print(users)

def checkLength(length1, length2):              #method for checking length of parameters. this is for checking if there are lost packets
        if(length1 == length2):
                return True
        return False

def main():
        connected = True
        while connected:
                msg = sock.recv(1024)                                                           #receive header from client
                
                header = msg                     
                header = header.decode('utf-8') 
                header = json.loads(header)
                if (checkLength(len(header['message']), header['length'])):                     #this is inaccurate. this should check if the header lost any packets during transfer
                        if (header['command'] == 1):                                            #enters login through opcommand
                                login(users, header['username'])
                        else:
                                if (header['message'] == DISCONNECT):                           #enters logout through opcommand
                                        logout(users, header['username'])
                                
                                elif (header['message'] == 'SHUT DOWN'):                        #shuts down through opcommand
                                        print("Server has shut down!")
                                        connected = False
                                else:
                                        print(header['username'] + ': '+ header['message'])     #prints sent message
                                        
        sock.close()


main()

