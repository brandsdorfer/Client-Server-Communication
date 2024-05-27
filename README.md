# client will get a message from the user and send it to the server then the client will print the response from the server

+ server protocol
* any request: server will return "no response".
* "hello" (not case sensitive): server will return "hello from server"
* "stop" (not case sensitive): server will stop the process immediately after sending the response "Server stopped". the client process will also stop immediately.
* "exit" (not case sensitive): client will exit but server will still be running

+ note!
the server is able  to communicate only with a single client!