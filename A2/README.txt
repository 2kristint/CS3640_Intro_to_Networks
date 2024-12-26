To run the application:
    python3 server.py 5000
        server.py script takes in one input parameter, the port number
    *open another terminal and run:
    python3 client.py localhost 5000
        client.py script should take two input parameters: the server’s IP address (use localhost for testing) and the port number

CREDIT REEL:
    https://www.cs.dartmouth.edu/~campbell/cs50/socketprogramming.html
    - set up server socket by creating a TCP socket using socket()
    - create TCP socket on client side using socket()
    - create connection between server and client using connect()
    - send inputted messages to the server and broadcast messages from server using send() and recv()
    https://realpython.com/intro-to-python-threading/ and 
        https://docs.python.org/3/library/threading.html and 
        https://martinxpn.medium.com/synchronizing-threads-in-python-with-locks-69-100-days-of-python-611a56a8430a#:~:text=When%20multiple%20threads%20try%20to,shared%20resource%20at%20a%20time.
    - allow server to broadcast to multiple clients using threading module
    https://supersourcing.com/blog/what-is-r-in-python-what-is-its-purpose/
    - clean prompting of user
    https://www.geeksforgeeks.org/file-flush-method-in-python/
    - writing to file

