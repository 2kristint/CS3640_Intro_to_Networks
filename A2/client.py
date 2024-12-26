import socket
import sys
import threading

MAXLINE = 4096 #max text line length
open = True 

def send_message(sockfd):
    global open
    while True:
        message = input("Enter message to send: ")
        if message == '/exit':
            sockfd.send(message.encode())
            open = False
            sockfd.close()
            break
        else:
            try:
                sockfd.send(message.encode())
            except:
                print("Error sending message.")
                break

def receive_message(sockfd):
    global open
    while True:
        try:
            response = sockfd.recv(MAXLINE)
            if not response:
                print("Server closed the connection or no data received.")
                break
            
            #clear current input prompt
            sys.stdout.write("\r" + " " * 40 + "\r")
            
            #print received message
            print("Received:", response.decode())
            sockfd.send(f"LOG: Received: {response.decode()}".encode())

            #display prompt again
            print("Enter message to send: ", end="")
            sys.stdout.flush()
        except:
            #check if socket is open
            if open == True:
                print("Error receiving message")
            break
    sockfd.close()

def run_client():
    #check arguments
    if (len(sys.argv) != 3):
        print("Usage: TCPClient <IP address of the server>")
        return
    IPAddress = sys.argv[1]
    portNum = sys.argv[2]

    #create TCP socket - socket()
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        print("Problem in creating the socket.")
        return
    
    #connect to server - connect()
    try: 
        sockfd.connect((IPAddress, int(portNum)))
    except:
        print("Problem in connecting to the server.")
        return
    
    #create threads
    sendThread = threading.Thread(target=send_message, args=(sockfd,))
    receiveThread = threading.Thread(target=receive_message, args=(sockfd,))

    sendThread.start()
    receiveThread.start()

    #wait for threads to finish before closing socket
    sendThread.join()
    receiveThread.join()

    sockfd.close()
    print("Connection closed.")
    


run_client()