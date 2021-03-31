import pickle
import socket

print('Server start')
sock = socket.socket()
port = 9064

while True:
    try:
        sock.bind(('', port))
        print('Port connected', port)
        break
    except OSError:
        port += 1

sock.listen(0)
sent = ''

f = open('users', 'w')
users = open("users", "rb")
try:
    users = pickle.load(users)
except EOFError:
    user = {}

while True:
    print('Client connection')
    conn, addr = sock.accept()
    print('connected:', addr)
    username = user.get(addr[0])
    if username:
        conn.send(f'User -  {username},  welcome back'.encode())
    else:
        conn.send(f'Enter your nickname: '.encode())
        data = conn.recv(1024)
        user.setdefault(addr[0], data.decode())
        users = open("users", "wb")
        pickle.dump(user, users)
        users.close()
        conn.send(f'Hi, {user.get(addr[0])}'.encode())
    while True:
        print('Receiving data')
        data = conn.recv(1024)
        print(data)
        if not data:
           break
        sent += data.decode()
        print('Sending data')
        conn.send(data)
    print(sent)
    conn.close()