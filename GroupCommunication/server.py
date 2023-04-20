import socket, threading

LOCALHOST = "127.0.0.1"
PORT = 9999

# Creating socket instance
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((LOCALHOST,PORT))
server.listen(1)

print("Server has started")

# list to keep track of all connected clients

clients = []

# function to handle client connections

def handle_client(client,address):

    while True:

        # Receiving message from the client
        msg = client.recv(1024)
        if not msg:
            # client has disconnected
            if client in clients:
                print("\nClient {} disconnected".format(address))
                clients.remove(client)
                break

            print("\n Message from Client {}:{}".format(address,msg.decode('utf-8')))

            # broadcasting message to all other clients
            for c in clients:
                if c != client:
                    msg = "Client " + address + ": " + msg.decode('utf-8')
                    c.send(msg.encode('utf-8'))
                client.close()

# main loop to accept client connections

while True:

    client,address = server.accept()
    print("\nClient {} connected.".format(list(address)[0]))
    clients.append((client))

    # creating a thread to handle each client connection

    thread = threading.Thread(target = handle_client, args = (client,list(address)[0]))
    thread.start()