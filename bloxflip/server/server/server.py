import socket
import threading

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 4782 # Arbitrary non-privileged port

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind((HOST, PORT))

# Listen for incoming connections
sock.listen()
print('Server listening on port', PORT)

def handle_client(connection, address):
    print('Connected by', address)

    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print('{}: {}'.format(address, data.decode()))

    # Clean up the connection
    connection.close()
    print('Connection closed by', address)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, address = sock.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(connection, address))
    client_thread.start()