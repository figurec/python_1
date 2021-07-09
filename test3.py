import socket
import os

HOST = ''
PORT = int(os.environ.get("PORT", 5000))
print("PORT: ", PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
sock.bind((HOST, PORT))
sock.listen(1)
while True:
  conn, addr = sock.accept()
  while True:
    data = conn.recv(1024)
    print(data)
    conn.close()
    break
