import socket
import random

# Create a TCP socket and start listening for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9000))
server_socket.listen(1)

# Accept incoming connections from clients
while True:
    print("Waiting for client to enter what they want...")
    client_socket, address = server_socket.accept()
    print("Client connected:", address)

    # Receive the message from the client
    client_message = client_socket.recv(1024).decode('utf-8')
    client_name, client_num = client_message.split(",")
    print("Client Name:", client_name)
    print("Server Name: Server of John Q. Smith")

    # Pick a random number between 1 and 100
    server_num = str(random.randint(1, 100))

    # Display the client's number, the server's number, and the sum
    print("Client Number:", client_num)
    print("Server Number:", server_num)
    sum = int(client_num) + int(server_num)
    print("Sum:", sum)

    # Send the server's name and number back to the client
    server_message = "Server of John Q. Smith," + server_num
    client_socket.send(bytes(server_message, 'utf-8'))

    # Check if the client's number is out of range
    if int(client_num) < 1 or int(client_num) > 100:
        print("Client Number is out of range")
        break

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()