import socket
import sys
import threading
import queue

MAXLINE = 4096  #max text line length
LISTENQ = 8  #maximum number of client connections
localhost = '127.0.0.1'

#create queue for broadcasting
messageQueue = queue.Queue()
#list of connected clients
clients = []
clientsLock = threading.Lock() #lock to synchronize access to clients list

f = open("output.txt", "w")

def file_write(message):
    try:
        print(message)
        f.write(message + '\n')
        f.flush()
    except:
        print("Error writing to file.")

def handle_client(connfd, cliaddr, f):
    #add client
    with clientsLock:
        clients.append(connfd)

    try:
        while True:
            buf = connfd.recv(MAXLINE)
            if not buf or buf.decode().startswith("/exit"):
                file_write(f"Disconnected from client: {cliaddr}")
                break
            else:
                #check if message is a log
                if buf.decode().startswith("LOG: "):
                    file_write(f"Log from {cliaddr}: {buf.decode()}")
                else:
                    file_write(f"Recieved from {cliaddr}: {buf.decode()}")
                    #put recieved message into queue
                    messageQueue.put((connfd, buf))
    except:
        file_write(f"Connection disconnected from the client: {cliaddr}")
    finally:
        #remove client
        with clientsLock:
            if connfd in clients:
                clients.remove(connfd)
        connfd.close()
        file_write(f"Connection with {cliaddr} closed.")

def broadcast():
    while True:
        connfd, message = messageQueue.get()
        if message == b'/exit':
            continue
        with clientsLock:
            for client in clients:
                if client != connfd:
                    try:
                        client.send(message)
                    except:
                        pass


def run_server():

    #output.txt
    #create file and write to it
    f.write("kto, Kristin To.\n")

    #check arguments
    if (len(sys.argv) != 2):
        file_write("Usage: TCPClient <IP address of the server>")
        sys.exit(1)
    portNum = sys.argv[1]

    #create TCP socket - socket()
    try:
        listenfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except:
        file_write("Problem in creating the socket for the server.")
        sys.exit(1)
    
    #bind socket to localhost on specified port - bind()
    listenfd.bind((localhost, int(portNum)))

    #listen for incoming connections - listen()
    listenfd.listen(LISTENQ)
    file_write("Server running...waiting for connections.")

    #start message broadcasting thread
    broadcastThread = threading.Thread(target=broadcast)
    broadcastThread.start()

    #accept()
    while True:
        #connfd - new socket object for specific client, cliaddr - client's address
        connfd, cliaddr = listenfd.accept()
        file_write(f"Connected with client {cliaddr}")

        clientThread = threading.Thread(target=handle_client, args=(connfd, cliaddr, f)) 
        clientThread.start()
    


run_server()

f.close()