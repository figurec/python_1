import socket
import os

HOST = "xhaus.com"
PORT = 80
#http://www.xhaus.com/headers
headers = b"GET /headers HTTP/1.1\r\n"
headers += b"Host: xhaus.com\r\n\r\n"
buffer = b""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
try:
  s.connect((HOST, PORT))
  s.sendall(headers)
  while True:
    in_recv = s.recv(1024)
    if in_recv:
      buffer += in_recv
    else:
      break
    #print(repr(buffer))
  s.close()
except socket.error as err:
  print("error socket", err)
  s.close()

HOST = ''
PORT = int(os.environ.get("PORT", 16903))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
sock.bind((HOST, PORT))
sock.listen()
client, addr = sock.accept()
id_data = client.recv(1024)
client.sendall(buffer)
client.close()
sock.close()
