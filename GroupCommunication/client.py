import socket,threading

HOST = "127.0.0.1"
PORT = 9999

# Creating socket instance
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connecting to the server
client.connect((HOST,PORT))

print("\nClient connected to the server {}".format(HOST))

# function to receive the message from server

def receive_messages():

    while True:
        try:
            # receive message from server
            msg = client.recv(1024)

            # print msg to console
            print(msg.decode('utf-8'))
            print()

        except:

            # closing connection if error occurs
            client.close()
            break

    # Creating a thread to receive messages from server

    thread = threading.Thread(target=receive_messages())
    thread.start()

    # main loop to send messages to server
    while True:
        print()
        message = input()

        # send msg to server
        client.send(message.encode('utf-8'))