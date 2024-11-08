import socket

# Server settings
host = 'localhost'
port = 12345
buffer_size = 1024  # Size of each packet

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

print(f"Server is listening on {host}:{port}")

# Receive file name from the client
filename, client_address = server_socket.recvfrom(buffer_size)
filename = filename.decode('utf-8')
print(f"Receiving file: {filename} from {client_address}")

# Open a file to write the received data
with open(f"received_{filename}", 'wb') as f:
    while True:
        # Receive the file data in chunks
        data, _ = server_socket.recvfrom(buffer_size)
        
        # If the data is empty, the file has been fully received
        if not data:
            break

        # Write data to the file
        f.write(data)

print(f"File received and saved as 'received_{filename}'")
server_socket.close()
