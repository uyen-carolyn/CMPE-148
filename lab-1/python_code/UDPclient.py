from socket import *
port = 12000
IP_address = gethostbyname(gethostname())
clientSocket = socket(AF_INET, SOCK_DGRAM) #create udp client socket
serverAddress =(IP_address,port)

while True:
    year = input('Enter a textfile containing the test cases. Type exit to close: ')
    if (year != "exit"):
        with open(year, 'r') as file:
            year = file.read()
    clientSocket.sendto(year.encode('utf-8'), serverAddress)
    resp, serverAddress = clientSocket.recvfrom(2048)
    resp = resp.decode('utf-8')
    print('Received from server:')
    if(resp == "Exit"):
        print(resp)
        break
        sys.exit()
    else:
        print(resp)

clientSocket.close()
