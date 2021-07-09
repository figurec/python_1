import socket

HOST = ''
PORT = int(os.environ.get("PORT", 5000))
print("PORT: ", PORT)

buffer = ""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("example.com", 80))

server.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n")

while True:
  data = server.recv(1024)
  if data:
    buffer += data
  else:
    break
server.close()
print(data)
