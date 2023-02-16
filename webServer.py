from socket import *

import sys

def webServer(port=13331):

  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(("", port))
  serverSocket.listen(1)

  while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(connectionSocket)
    print(addr)
    
    try:
      message = connectionSocket.recv(1024).decode()
      print(message)
      filename = message.split()[1]

      f = open(filename[1:], "r")
      print(f)

      outputdata = b"Content-Type: text/html; charset=UTF-8\r\n"
      statuscode = b"HTTP/1.1 200 OK\r\n"

      for i in f:
        print(i)
        connectionSocket.sendto(i.encode(), addr)
        connectionSocket.sendto(outputdata.encode(), addr)
        connectionSocket.sendto(statuscode.encode(), addr)
      connectionSocket.close()
      
    except Exception as e:
      errMssg = '404 file not found'
      connectionSocket.sendto(errMssg.encode(), addr)
    connectionSocket.close()

if __name__ == "__main__":
  webServer(13331)
