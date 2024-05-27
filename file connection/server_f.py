FILENAME = "./connection.txt"

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
    
def return_response():
    """
    This function is responsible for handling client requests and sending responses.
    It reads from a file (connection.txt) and waits for a client request.
    Once a request is received, it processes the request using the response_by_req function.
    The response is then written back to the file.
    The function continues to loop until a stop request is received.

    Returns:
    int: 1 if the server is stopped, 0 otherwise.
    """

    # loop running until the file is written by the client - 
    # Identified by the opening letter (C: means client, S: means server)
    while True:
        
        try:
            # Open the file in read mode
            clientf = open(FILENAME, 'r')
            
            # Read the content of the file
            data = clientf.read()
            
            # checks if the client side content is written 
            if data and data[0] == "C":
                print("conecting whith client" )
                print("The client sent :" + data)

                # use the protocol to respond accordingly
                res = response_by_req(data[3:])
                
                # Close the file
                clientf.close()
                
                # Break the loop if a response is ready
                break

        except FileNotFoundError:
            # Continue the loop if the file is not found
            continue
    
    # Open the file in write mode
    serverf = open(FILENAME, 'w')
    
    # Write the response to the file
    serverf.write(f"S: {res}")
    
    # Close the file
    serverf.close()

    # return a status to use in case of a stop request
    if res == "Server Stopped":
        print("Server Stopped")
        return 1
    else:
        return 0
    
def main():
    print("the server is running ...")
    
    # define the variable of status use in case of stopping the server
    status = 0

    # Server is running waiting for requests
    while status != 1:
         # Call the return_response function to handle client requests and get the status
        status = return_response()


if __name__ == '__main__':
    main()