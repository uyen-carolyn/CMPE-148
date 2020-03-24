from socket import *
port = 12000
IP_address = gethostbyname(gethostname())
clientSocket = socket(AF_INET, SOCK_DGRAM) #create udp client socket
serverAddress =(IP_address,port)

while True:
    year = input('Enter a set of years with a comma in between each year. Type exit to close: ')
    clientSocket.sendto(year.encode('utf-8'), serverAddress)
    res, serverAddress = clientSocket.recvfrom(2048)
    res = res.decode('utf-8')
    print('Received from server:')
    if(res == "Exit"):
        print(res)
        break
        sys.exit()
    else:
        print(res)

clientSocket.close()
