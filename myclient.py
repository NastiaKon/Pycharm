import socket

sock = socket.socket()

address = 'localhost'
port = input('Input port: ')
#ort = 9000
if not port:
    port = 9000
else:
    port = int(port)

sock.setblocking(True)
sock.connect((address, port))
print('Server connection')

while True:
    sent = input('Input sentence: ')
    if sent == 'exit':
        sock.close()
        print('Disconnection')
        break
        
    sock.send(sent.encode())
    data = sock.recv(1024)
    print(data.decode())
    print('Receiving data')

print('Sending data')



