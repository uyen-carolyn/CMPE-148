from socket import *
import sys
port = 10000
IP_adress = gethostbyname(gethostname())
clientSocket = socket(AF_INET, SOCK_STREAM)

client_address =(IP_adress,port)
clientSocket.connect(client_address)

while True:
    year = input('Enter a textfile containing the test cases. Type exit to close: ')
    if (year != "exit"):
        with open(year, 'r') as file:
            year = file.read()
    clientSocket.send(year.encode('utf-8'))
    resp = clientSocket.recv(1024).decode('utf-8')
    print('Received from server:')
    if(resp == "Exit"):
        print(resp)
        break
        sys.exit()
    else:
        print(resp)

clientSocket.close()
