import socket

sock = socket.socket()
port = 9000
while True:
    try:
        sock.bind(('', port))
        break
    except OSError:
        port += 1

print('Server start')       
sock.listen(1)
print('Port connected')


while True:
    print('Client connection')
    conn, addr = sock.accept()
    print('connected:', addr)
    while True:
        data = conn.recv(1024)
        print('Receiving data')
        if not data:
           break
        print('Sending data')
        conn.send(data)
        print(data.decode())

