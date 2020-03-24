from socket import *
import sys

port = 10000
IP_address = gethostbyname(gethostname())

serverSocket = socket(AF_INET, SOCK_STREAM)
server_address = (IP_address,port)
serverSocket.bind(server_address)
serverSocket.listen(1)

print('Server ready! ')

def find_leap_year(y):
    year = list(map(int, y.split(",")))
    for i in year:
        if (i % 4 == 0):          # leap years are divisible by 4,100,and 400, or 4 but not 100.
            if (i % 100 == 0):    # non-Leap years are not divisible by 4 or is divisible by 4 and 100 but not 400.
                if (i % 400 == 0):
                    print ('Year {} is a leap year!'.format(i))
                else:
                    print ('Year {} is not a leap year!'.format(i))
            else:
                print ('Year {} is a leap year!'.format(i))
        else:
            print ('Year {} is not a leap year!'.format(i))

    return "That's all"

connectionSocket, address = serverSocket.accept()  # listen and accept port from client

while True:
    y = connectionSocket.recv(1024).decode('utf-8')

    try:
        if (y == 'exit'):
            print('The client wants to exit')
            resp = "Exit"
            connectionSocket.send(resp.encode('utf-8'))
            sys.exit()
        else:
            print('Received the following: {!r}'.format(y))
    except ValueError:
        print('Received invalid values. Please try again.')
    else:
        try:
            resp = find_leap_year(y)
            connectionSocket.send(resp.encode('utf-8'))
        except ValueError:
            resp = "Received invalid values. Please try again."
            connectionSocket.send(resp.encode('utf-8'))
        else:
            print('Success. Send the results back to the client!')

serverSocket.close()
