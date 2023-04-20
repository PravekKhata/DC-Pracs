
import  socket

# Use localhost IP address and port no.

LOCALHOST = "127.0.0.1"
PORT = 8080

# Calling the server socket method

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((LOCALHOST,PORT))
server.listen(1)

print("Server started")
print("Waiting for client request")

# Server socket ready for getting input from the user

clientConnection, clientAddress = server.accept()
print("Client Connected: ",clientAddress)
msg = ""

# Receiving the data from client and then creating arithmetic operations

while True:

    data = clientConnection.recv(1024)
    msg = data.decode()

    print("Equation received")
    result = 0

    # Splitting the received equation to calculate the result
    operation_list = msg.split()
    oprd1 = operation_list[0]
    oprd2 = operation_list[2]
    operation = operation_list[1]

    # Changing str to int

    num1 = int(oprd1)
    num2 = int(oprd2)

    if(operation == "+"):
        result = num1 + num2
    elif(operation == "-"):
        result = num1 - num2
    elif(operation == "*"):
        result = num1 * num2
    elif(operation == "/"):
        result = num1 / num2

    # printing the result

    print("The result is: ", result)

    # Sending result to the client
    print()
    print("Sending the result to the client..")

    # Changing int to string and after encoding send output to client
    output = str(result)
    clientConnection.send(output.encode())

clientConnection.close()
