import socket
import selectors

selector = selectors.DefaultSelector()


def server() -> None:
    """Server definition."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))  # socket file is created
    server_socket.listen()

    selector.register(fileobj=server_socket,
                      events=selectors.EVENT_READ,
                      data=accept_connection)


def accept_connection(socket_server: socket.socket) -> None:
    # creating a client socket
    client_socket, addr = socket_server.accept()
    print('Connection from:', addr)

    selector.register(fileobj=client_socket,
                      events=selectors.EVENT_READ,
                      data=send_message)


def send_message(socket_client: socket.socket) -> None:
    request: bytes = socket_client.recv(4096)
    if request:
        client_address = socket_client.getpeername()[1]
        input_message = request.decode().replace('\n', '')
        print(f"Client {client_address} sent me it: {input_message}")
        response = f'Server answer you, dear {client_address}\n'.encode()
        socket_client.send(response)
    else:
        selector.unregister(socket_client)
        socket_client.close()


def event_loop():
    print('Loop started...')

    while True:
        # choose events ready for reading
        events: list[tuple[selectors.SelectorKey, int]] = selector.select()
        print(events[0][0].fileobj.getpeername())

        # Key is Namedtuple, has 3 field: fileobj, events, data
        for key, _ in events:
            callback = key.data
            print(callback)
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
