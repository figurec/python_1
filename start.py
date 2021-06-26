PORT = int(os.environ(['PORT']))

import socket

sock = socket.socket()
sock.bind(('', PORT))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
