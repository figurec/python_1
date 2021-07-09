import socket

HOST = "xhaus.com"
PORT = 80
#http://www.xhaus.com/headers
headers = b"GET /headers HTTP/1.1\r\n"
headers += b"Host: xhaus.com\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
try:
  s.connect((HOST, PORT))
  s.sendall(headers)
  buffer = b""
  while True:
    in_recv = s.recv(1024)
    if in_recv:
      buffer += in_recv
    else:
      break
    print(repr(buffer))
  s.close()
except socket.error as err:
  print("error socket", err)
  s.close()
