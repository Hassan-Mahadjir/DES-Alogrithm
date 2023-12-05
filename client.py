import socket

# Set the host and port
host = '127.0.0.1'
port = 12345

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send data to the server
message = "Hello, serverrr!"
client_socket.send(message.encode('utf-8'))

# Close the connection
# client_socket.close()
