import socket, select

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
headleng=10
s.bind((socket.gethostname(), 8888))
s.listen(10)
sockets_list = [s]
clients = {}
def get_rps(client_socket):
    try:
        header = client_socket.recv(headleng)

        if not len(header):
            return False

        lengthmsg= int(header.strip())
        return {"header": header, "data": client_socket.recv(lengthmsg)}
    except:
        return False


while True:
    read_sockets, _, exceptionsockets = select.select(sockets_list, [], sockets_list)
    for not_sock in read_sockets:
        if not_sock == s:
            client_socket, client_address = s.accept()
            user = get_rps(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)

            clients[client_socket] = user

            print (f"Accepted new connection from {client_address[0]}:{client_address[1]} Name:{user['data']}")
        else:
            message = get_rps(not_sock)

            if message is False:
                print(f"Closed connection from {clients[not_sock]['data']}")
                sockets_list.remove(not_sock)
                del clients[not_sock]
                continue

            user = clients[not_sock]
            print(f"Recieved message from {user['data']}: {message['data']}")

            for client_socket in clients:
                if client_socket != not_sock:
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
    for not_sock in exceptionsockets:
        sockets_list.remove(not_sock)
        del clients[not_sock]