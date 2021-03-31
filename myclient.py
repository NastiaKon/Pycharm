import socket

sock = socket.socket()
sock.setblocking(1)

#address = 'localhost'
while True:
    try:
        port = int(input('Input port: '))
        address = input('Input hostname: ')
        sock.connect((address, port))
        print('Server connection', file=open('config.txt', 'a'))
        break
    except socket.gaierror:
        address = '192.168.68.27'
        port = 9064
        print('Incorrect data, open socket with port = ', port, ', address - ', address)
        try:
            sock.connect((address, port))
            break
        except OSError:
            port += 1
    except ConnectionRefusedError:
        print('Smth went wrong, try again')


data = sock.recv(1024).decode()
if 'Enter your nickname:' in data:
    print(data)
    name = input('Nickname: ')
    sock.send(name.encode())
    print(sock.recv(1024).decode())


while True:
    sent = input('Input sentence: ')
    if sent == 'exit':
        sock.close()
        print('Disconnection', file=open('config.txt', 'a'))
        break
    sock.send(sent.encode())
    print('Sending data', file=open('config.txt', 'a'))
    data = sock.recv(1024)
    print('Receiving data', file=open('config.txt', 'a'))
    print(data.decode())
print('Disconnection', file=open('config.txt', 'a'))

