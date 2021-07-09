import socket
import selectors

import threading
import time

import os

HOST = ''  # The server's hostname or IP address
#PORT = 16903        # The port used by the server
PORT = int(os.environ.get("PORT", 5000))
print("PORT: ", PORT)

CLASS_COUNT = 0

sel = selectors.DefaultSelector()

class worker:
  def __init__(self, sock):
    global CLASS_COUNT
    CLASS_COUNT += 1
    print("constructor [", CLASS_COUNT, "]")
    #variable
    self.state = 10
    self.client_buffer = []
    self.server_buffer = []
    self.client_reg = True
    self.server_reg = False
    self.events = selectors.EVENT_READ | selectors.EVENT_WRITE
    #client
    self.client, self.addr = sock.accept()
    self.client.setblocking(False)
    sel.register(self.client, self.events, data=self)
    #server
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #self.server.setblocking(False)
    #sel.register(self.server, events, data=self)
    
  def __del__(self):
    global CLASS_COUNT
    CLASS_COUNT -= 1
    print("destructor [", CLASS_COUNT, "]")

  def sockets_close(self):
    if self.client_reg == True:
      self.client_reg = False
      sel.unregister(self.client)
    if self.server_reg == True:
      self.server_reg = False
      sel.unregister(self.server)
    self.client.close()
    self.server.close()
    self.state = 0
    
  def get_domain_port(self, request):
    #from string Cookie
    if request.find(b"\r\n\r\n") != -1:
      pos1 = request.find(b"Cookie:") + len(b"Cookie:")
      pos2 = request.find(b"\r\n", pos1)
      res = request[pos1:pos2].strip().split(b"^") #^ delim
      if len(res) == 2:
        return ( res[0], int(res[1]) )
      else:
        return (None, None)

  def sockets_event(self, key, mask):
    sock = key.fileobj
    if sock == self.client:
      func_read = self.client_read
      buffer = self.client_buffer
      sock_str = "client"
    else:
      func_read = self.server_read
      buffer = self.server_buffer
      sock_str = "server"
    if mask & selectors.EVENT_READ:
      try:
        recv_data = sock.recv(1024)
        if recv_data:
          func_read(recv_data)
        else:
          print("sockets_event: read close", sock_str)
          self.sockets_close()
      except socket.error as err:
        print("sockets_event: error read", err, sock_str)
        self.sockets_close()
    if mask & selectors.EVENT_WRITE:
      try:
        if len(buffer) > 0:
          sock.sendall( buffer.pop(0) )
        if self.state == 0:
          self.sockets_close()
      except socket.error as err:
        print("sockets_event: error write", err, sock_str)
        self.sockets_close()
  
  def client_read(self, recv_data):
    if self.state == 10:
      host, port = self.get_domain_port(recv_data)
      if host is not None and port is not None:
        print(host, port)
        print(recv_data)
        self.state = 20
        try:
          self.server.connect((host, port))
          self.server.setblocking(False)
          self.server_reg = True
          sel.register(self.server, self.events, data=self)
        except socket.error as err:
          self.sockets_close()
        self.client_buffer.append(b"HTTP/1.1 200 OK\r\n\r\n")
      else:
        self.state = 0
        self.client_buffer.append(b"HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nERROR PAGE Its My Page") # страница заглушка
    elif self.state == 20:
      self.server_buffer.append( recv_data )
    
  def server_read(self, recv_data):
    if self.state == 20:
      self.client_buffer.append( recv_data )



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
sock.bind((HOST, PORT))
sock.listen()
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, data=None)

while True:
  events = sel.select(timeout=None)
  for key, mask in events:
    if key.data is None:
      cls = worker(sock)
      cls = 0
    else:
      key.data.sockets_event(key, mask)
      
