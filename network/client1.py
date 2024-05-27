from socket import *

PORT = 3000

# in this case that the server is running on the same computer
HOST = gethostname()


def main():
    
    
    while True:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        msg = input("Enter the message to be sent to the server : ")
        client_socket.send(msg.encode())
        
        if msg == "stop":
           break

        try:
          data = client_socket.recv(1024).decode()
          print("The server sent :\n" + data)

        except ConnectionRefusedError:
          print(error)


    client_socket.close()
    print("conecting closed")

if __name__ == "__main__":
  main()