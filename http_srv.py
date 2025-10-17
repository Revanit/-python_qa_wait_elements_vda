import socket
import datetime



# Create a TCP server socket

http_response = (
        f"HTTP/1.0 200 OK\r\n"
        f"Server: otusdemo\r\n"
        f"Date: Sat, 01 Oct 2022 09:39:37 GMT\r\n"
        f"Content-Type: text/html; charset=UTF-8\r\n"
        f"\r\n"
        )

end_of_stream = '\r\n\r\n'

def handle_client(connection):
    client_data = ''
    with connection:
        while True:
            data = connection.recv(1024)
            print("Received:", data)
            if not data:
               break
            client_data += data.decode()
            if end_of_stream in client_data:
                break
        # Send current server time to the client
        serverTimeNow = "%s"%datetime.datetime.now();
        connection.send(http_response.encode() 
                + serverTimeNow.encode() 
                + f"\r\n".encode())
        #print("Sent %s to %s"%(serverTimeNow, clientAddress));


with socket.socket() as serverSocket:
    # Bind the tcp socket to an IP and port
    serverSocket.bind(("127.0.0.1", 40404));
    # Keep listening
    serverSocket.listen();

    while(True): # Keep accepting connections from clients
        (clientConnection, clientAddress) = serverSocket.accept();
        handle_client(clientConnection)
        print(f"Sent data to {clientAddress}");
