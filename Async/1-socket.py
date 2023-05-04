import socket

# socket [127.0.0.0:5000] = domain [127.0.0.0] + port [5000]

# server definition
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('----- Before .accept() -----')
    client_socket, addr = server_socket.accept()
    print('Connection from: ', addr)

    while True:
        print('----- Before .recv() -----')
        request = client_socket.recv(4096)
        print(f"<{addr[1]}> sent me it: {request.decode()}")

        if not request:
            break
        else:
            response = 'Server answer you\n'.encode()
            client_socket.send(response)

    print('Outside inner while loop')
    client_socket.close()
