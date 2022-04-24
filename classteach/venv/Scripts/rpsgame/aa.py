import socket, select, errno,sys

headlength = 10

name = input("Name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("107.202.105.8", 8888))
client_socket.setblocking(False)

name_header = f"{len(name):<{headlength}}"
client_socket.send(name_header + name)

while True:
    message = input(f"{name} > ")

    if message:
        message_header = f"{len(message):<{headlength}}"
        client_socket.send(message_header + message)
    try:
        while True:
            name_header = client_socket.recv(headlength)
            if not len(name_header):
                print("Connection closed by server host")
                sys.exit()
            name_lengt  
    except:
        pass