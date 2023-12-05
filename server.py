from decryption import DESDecryption

import socket

# Set the host and port
host = '127.0.0.1'
port = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

# Receive data from the client
data = client_socket.recv(1024)
isExtensionRequired = (len(data) % 8 != 0)

result_of_decryption = DESDecryption(
    key='12345678', text=data, extension=isExtensionRequired)
print(f"Received data: {data.decode('utf-8')}")

# Close the connection
client_socket.close()
