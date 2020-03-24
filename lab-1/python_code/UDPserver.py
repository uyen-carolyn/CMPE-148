from socket import *
import sys

port = 12000

print('IP Address: ', gethostbyname(gethostname()))
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((gethostbyname(gethostname()), port))
print("The server is ready!")

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

while True:
    y, clientAddress = serverSocket.recvfrom(2048)
    y = y.decode('utf-8')

    try:
        if ((y == 'exit')):
            print('The client wants to exit')
            resp = "Exit"
            serverSocket.sendto(resp.encode('utf-8'),clientAddress)
            sys.exit()
        else:
            print('Received the following years: {!r}'.format(y))
    except ValueError:
            print('Invalid values. Please try again.')
            serverSocket.sendto("Invalid values. Please try again.",clientAddress)
    else:
        try:
            resp = find_leap_year(y)
            print(resp)
            serverSocket.sendto(resp.encode('utf-8'),clientAddress)
        except ValueError:
            resp = "Invalid values. Please try again."
            serverSocket.sendto(resp.encode('utf-8'), clientAddress)
        else:
            print('Success. Send the result back to the client!')
serverSocket.close()
