import socket

# Get the client name and integer from the user
name = input("Enter your name: ")
num = input("Enter an integer between 1 and 100: ")

# Open a TCP socket and send the message to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9000))
client_socket.send(bytes(name + "," + num, 'utf-8'))

# Wait for the server's reply
server_reply = client_socket.recv(1024)
server_name, server_num = server_reply.decode('utf-8').split(",")

# Print the results and compute the sum
print("Client Name:", name)
print("Server Name:", server_name)
print("Client Number:", num)
print("Server Number:", server_num)
sum = int(num) + int(server_num)
print("Sum:", sum)

# Close the client socket
client_socket.close()