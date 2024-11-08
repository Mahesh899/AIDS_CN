import socket
import os

# Client settings
server_host = 'localhost'
server_port = 12345
buffer_size = 1024  # Size of each packet

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# File to send
filename = 'file.txt'

# Check if the file exists
if not os.path.isfile(filename):
    print(f"File '{filename}' not found!")
    exit()

# Send the filename first
client_socket.sendto(filename.encode('utf-8'), (server_host, server_port))

# Send the file data in chunks
with open(filename, 'rb') as f:
    while True:
        # Read the file in chunks of buffer_size
        data = f.read(buffer_size)
        
        # If data is empty, end of file
        if not data:
            break
        
        # Send the chunk to the server
        client_socket.sendto(data, (server_host, server_port))

# Notify the server that the file transfer is complete
client_socket.sendto(b'', (server_host, server_port))  # Sending empty byte to signal EOF

print(f"File '{filename}' sent to {server_host}:{server_port}")
client_socket.close()
