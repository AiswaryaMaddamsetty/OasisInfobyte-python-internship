# server.py
import socket
import threading

def handle_client(client_socket):
    while True:
# Receives message from client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print("Received:", message)
# Broadcasts message to all other clients
        for client in clients:
            if client != client_socket:
                client.send(message.encode('utf-8'))

# Creates a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binds the socket to a host and port
server_socket.bind(('localhost', 9999))
# Takes the incoming connections
server_socket.listen(5)
print("Server is listening...")

clients = []

while True:
# Accepts a new connection
    client_socket, address = server_socket.accept()
    print("Connected with", address)
    clients.append(client_socket)

# Starts a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
