import socket
from select import select
# <select> is needed to monitor changes in the state of file objects.
# In Unix everything is a file.

# server definition
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000)) # socket file is created
server_socket.listen()

# storage of available sockets
to_monitor = []

def accept_connection(socket_server: socket.socket) -> None:
    # creating a client socket
    client_socket, addr = socket_server.accept()
    print('Connection from:', addr)
    # add to client socket to storage
    to_monitor.append(client_socket)

def send_message(socket_client: socket.socket) -> None:
    request: bytes = socket_client.recv(4096)
    if request:
        client_address = socket_client.getpeername()[1]
        input_message = request.decode().replace('\n', '')
        print(f"Client {client_address} sent me it: {input_message}")
        response = f'Server answer you, dear {client_address}\n'.encode()
        socket_client.send(response)
    else:
        socket_client.close()

def event_loop():
    # add server socket
    to_monitor.append(server_socket)
    print('Loop started...')

    while True:
        # choose sockets ready for reading
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)
        s = [f"{i}.{s}\n" for i, s in enumerate(to_monitor, start=1)]
        print(f"Available sockets:\n{''.join(s)}")
if __name__ == '__main__':
    event_loop()