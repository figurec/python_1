import os
PORT = int(os.environ.get('PORT', 5000))
print("PORT: ", PORT)

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
