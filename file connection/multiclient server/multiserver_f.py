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
        res = False
        try:
            # Open the file in append mode (a+)
            # This allows us to read and write to the file without deleting its existing content
            clientf = open(FILENAME, 'a+')
            
            # Read the content of the file
            # readlines() returns a list of strings, where each string represents a line in the file
            data = clientf.readlines()

            for i in range(len(data)):
                # checks if the client side content is written 
                # The first character of each line is used to identify the sender (C: client, S: server)
                if data[i] and data[i][0] == "C":
                    print(f"Connecting with client with unique num {i}" )
                    print("The client sent :" + data[i])

                    # use the protocol to respond accordingly
                    # response_by_req function processes the client's request and returns a response
                    res = response_by_req(data[i][3:])
                    
                    # Prepare the server's response in the format "S: {res}\n"
                    data[i] = "S: {res}\n"
                    # Write the response to the file
                    # writelines() writes a list of strings to the file
                    clientf.writelines(data)
                    
                    # Close the file
                    clientf.close()
                    
                    # Break the loop if a response is ready
                    break
            if res:
                break
        except FileNotFoundError:
            # Continue the loop if the file is not found
            continue
    


    # return a status to use in case of a stop request
    # If the server received a stop request, return 1
    # Otherwise, return 0
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