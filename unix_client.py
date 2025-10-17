import os
import socket

SOCKET_FILE = '/tmp/echo.socket'

print(f"Connecting to {SOCKET_FILE}...")

if os.path.exists(SOCKET_FILE):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(SOCKET_FILE)
    print("Done.")

    print("Send 'DONE' to shut down server.")
    while True:
        try:
            input_data = input("> ")
            if "" != input_data:
                print("Sent: %s" % input_data)
                client.send(input_data.encode('utf-8'))
                if "DONE" == input_data:
                    break
        except KeyboardInterrupt as k:
            print("Turn off.")
            break
    client.close()
else:
    print("I can't connect!")
print("Done")
