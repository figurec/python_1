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
        data = sock.recv(1024 * 50)
        if not data:
            break
        buffer += data
    return buffer
    #print(data)


def client():
    opt = ("example.com", 80)
    cln = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #cln = socket.create_connection(opt);
    cln.connect(opt)
    h = b"GET / HTTP/1.1\r\n"
    h += b"Host: example.com\r\n\r\n"
    cln.sendall(h)
    res = read(cln)
    print(res)
    cln.close


import time


def main():
    print("main")
    #exit(0)
    start = time.time()
    client()
    print ("it took", time.time() - start, "seconds.")

if __name__ == "__main__":
    main()
