import socket
import time

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    msg = "Welcome to the server!"
    msg = f"{len(msg):<{HEADER_SIZE}}" + msg # the first 10 characters will act as the header to represent the message size

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)

        msg = f"The time is {time.time()}"
        msg = f"{len(msg):<{HEADER_SIZE}}" + msg # the first 10 characters will act as the header to represent the message size

        clientsocket.send(bytes(msg, "utf-8"))
