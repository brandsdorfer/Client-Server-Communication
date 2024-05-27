from socket import *

PORT = 3000
HOST = gethostname()
server_address = (HOST, PORT)

def response_by_req(data):
    """
    This function processes client requests and returns a response based on the protocol.

    Parameters:
    data (str): The client's request. It should be a string that matches the protocol.
    Returns:
    str: The server's response based on the client's request.
    """
    # this will be the protocol response 
    if data.lower() == "hello":
        return "Hello From Server"
    elif data.lower() == "stop":
        return "Server Stopped"
    else:
        return "no response"
    

def main():    

    # internet connection (AF_INET) - TCP (SOCK_STREAM)
    server_socket = socket(AF_INET, SOCK_STREAM)

    server_socket.bind(server_address)
    server_socket.listen()
    print("the server is running ...")

    
    while True:
        (communication_socket, client_address) = server_socket.accept()
        print(f"connecting with {client_address}")
        data = communication_socket.recv(1024).decode("utf-8")
        print("The client sent :" + data)

        res = response_by_req(data)
        if data == "stop":
            break

        communication_socket.send(res.encode())
        communication_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
