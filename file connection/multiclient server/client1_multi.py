import time
import os

FILENAME = "./connection.txt"
TIME_LIMIT_SEC = 60 # seconds

# an unique identifier for each client
UNIQUE_NUM =  len(open(FILENAME, 'r').readlines()) if os.path.exists(FILENAME) else 0

def check_timeout(timestart):
    # chek if timeout is reached
    return (time.time() - timestart)  > TIME_LIMIT_SEC

def nain():
    """
    This function acts as a client to communicate with a server.
    It sends messages to the server and waits for responses.
    The client continues to send messages until the server sends a "Server Stopped" message.

    Returns:
        None
    """

    # the server will receive data from the user until the command "stop" is executed 
    while True:
        
        # read the request from user    
        msg =  input("Enter the message to be sent to the server : ")
        if msg.lower() == "exit":
            raise SystemExit("you exit now the client")
        
        # Open the connection file in write mode to send a message to the server
        with open(FILENAME, 'a') as f:
            # Write the message to the file with a prefix 'C:' to indicate it's from the client
            f.write(f"C: {msg}\n")

        # Initialize the response variable with a default value indicating that the response is from the client
        res = "C"
        print("waiting for response...")

        # Define the start time of the process
        starttime = time.time()

        # Loop running until the file is written by the server - 
        # Identified by the opening letter (C: means client, S: means server)
        while res == "" or res[0] == "C":
            try:
                # Open the connection file in read mode to receive a response from the server
                with open(FILENAME, "r") as serverfile:
                    data = serverfile.readlines()

                if  data[UNIQUE_NUM][0] == "S":
                        res = data[UNIQUE_NUM]
                        break

            except PermissionError:
                # Change the permissions of the file to allow read and write access
                os.chmod(FILENAME, 0o770)
                continue
            
            

            # Check if the timeout is reached
            if check_timeout(starttime):
                # Raise a ConnectionError if the timeout is reached
                raise ConnectionError("ERROR! request timeout:\nCheck if server is running")
        
        # Output the server response if it's not from the client
        if res[0] == "S":
            print("The server sent :\n" + res[3:])

        # Check if the server stopped then stop the client
        if res[3:] == "Server Stopped":
            print("conecting closed")
            break


if __name__ == "__main__":
    nain()