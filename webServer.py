# import socket module
from socket import *
# In order to terminate the program
import sys
def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)

  #Fill in end

  while True:
    #Establish the connection
    
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?
    # #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode()

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?
      #Fill in start
      filename = message.split()[1]  # returns the first word in split only ignoring the GET
      #print(filename) #comment this out later

      fields = message.split("\r\n")
      fields = fields[1:]  # ignore the GET / HTTP/1.1
      message_headers = {}
      for field in fields:
        if not field:
          continue
        key, value = field.split(':', 1)
        message_headers[key] = value
      print(message_headers) #comment out later
      #Content-Type is an example on how to send a header as bytes. There are more!

      #opens the client requested file.
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      new_filename = filename.lstrip("/")
      file_to_open = open(new_filename, "rb") #fill in start #fill in end
      #fill in end
      


      print("file okay")
      outputdata = [b"HTTP/1.1 200 OK\r\n"]
      outputdata.append(b"Content-Type: text/html; charset=UTF-8\r\n")
      outputdata.append(b"message_headers['Connection']")
      outputdata.append(b"message_headers['Host']")
      #outputdata.append(b" ")
      outputdata.append(b"\r\n\r\n")

        #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end

      for i in file_to_open: #for line in file
      #Fill in start - append your html file contents #Fill in end
        line = file_to_open.readline()
        outputdata.append (line)
      outputdata.append(b"\r\n\r\n")


      #Send the content of the requested file to the client (don't forget the headers you created)!
      #Send everything as one send command, do not send one line/item at a time!

      # Fill in start
      message_out = bytes().join(outputdata)
      connectionSocket.send(message_out)
      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      print("file not found")
      outputdata = [b"HTTP/1.1 404 Not Found\r\n"]
      outputdata.append(b"Content-Type: text/html; charset=UTF-8\r\n")
      outputdata.append(b"message_headers['Connection']")
      outputdata.append(b"message_headers['Host']")
      outputdata.append(b"\r\n\r\n")
      message_out = bytes().join(outputdata)
      connectionSocket.send(message_out)

      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  # Commenting out the below (some use it for local testing). It is not required for Gradescope, and some students have moved it erroneously in the While loop. 
  # DO NOT PLACE ANYWHERE ELSE AND DO NOT UNCOMMENT WHEN SUBMITTING, YOU ARE GONNA HAVE A BAD TIME
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
