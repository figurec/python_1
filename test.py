import os
import selectors

sel = selectors.DefaultSelector()

PORT = int(os.environ.get('PORT', 5000))
print("PORT: ", PORT)

import socket

'''
def server():
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    serv_sock.bind(('', 53210))
    serv_sock.listen(10)

    while True:
        # Бесконечно обрабатываем входящие подключения
        client_sock, client_addr = serv_sock.accept()
        print('Connected by', client_addr)

        while True:
            # Пока клиент не отключился, читаем передаваемые
            # им данные и отправляем их обратно
            data = client_sock.recv(1024)
            if not data:
                # Клиент отключился
                break
            client_sock.sendall(b"data")

        client_sock.close()
'''


def read(sock):
    buffer = b""
    while True:
        try:
            data = sock.recv(10)
            if not data:
                #sock.close()
                break
            buffer += data
        except socket.timeout:
            print("socket.timeout")
            break
    return buffer
    #print(data)


def client():
    opt = ("example.com", 80)
    cln = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #cln = socket.create_connection(opt);
    cln.settimeout(5)
    #cln.setblocking(0)
    cln.connect(opt)
    h = b"GET / HTTP/1.1\r\n"
    h += b"Host: example.com\r\n"
    h += b"Connection: close\r\n\r\n" #close connection
    #cln.sendall(h)
    cln.send(h)
    res = read(cln)
    print(res)
    '''
    while True:
      data = cln.recv(2048)
      if not data: #close connection
        print("cln.close")
        break
      print(data)
    '''
    cln.close


import time


def main():
    print("\n")
    #exit(0)
    start = time.time()
    client()
    print ("\n", "it took", time.time() - start, "seconds.")

if __name__ == "__main__":
    main()


