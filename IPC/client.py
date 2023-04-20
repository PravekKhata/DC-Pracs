
import socket

SERVER = "127.0.0.1"
PORT = 8080

# Making socket instance

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connecting to the server

client.connect((SERVER,PORT))

while True:

    inp = input("\nEnter the operation in the form of (operand operation operand): ")

    if inp == "stop":
        break

    # Sending the input to the server socket using send method

    client.send(inp.encode())

    # Receiving output from server socket

    answer = client.recv(1024)
    print("\nAnswer is: ", answer.decode())

    print("\n Type 'stop' to terminate the process")

client.close()
