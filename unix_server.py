import os
import socket

SOCKET_FILE = '/tmp/echo.socket'

if os.path.exists(SOCKET_FILE):
    os.remove(SOCKET_FILE)

print(f"Opening Unix socket on {SOCKET_FILE}")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(SOCKET_FILE)

print("Listening...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print("-" * 20)
    print(datagram.decode("utf-8"))
    if b"DONE" == datagram:
        break

print("-" * 20)
print("Turning off...")
server.close()
os.remove(SOCKET_FILE)
print("Done")
