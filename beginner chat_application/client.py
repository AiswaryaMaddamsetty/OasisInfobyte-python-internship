import socket
import threading

def receive_messages():
    while True:
# Receives message from server
        message = client_socket.recv(1024).decode('utf-8')
        print("\n", message)

# Creates a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server
client_socket.connect(('localhost', 9999))
print("Connected to server.")

# Starts a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
# Sends message to server
    message = input("Enter message: ")
    client_socket.send(message.encode('utf-8'))
