import os
import socket

port = int(os.environ.get("PORT", 5000))
print("PORT: ", port)

def read(client_sock):
    buffer = ''
    while True:
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        buffer += data
    return buffer

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', port))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        #data = client_sock.recv(1024)
        #if not data:
            # Клиент отключился
            #client_sock.close()
            #break
        data = read(client_sock)
        print(data)
        #if data[0] == 10:
        #    result = b'this work'
        #else:
        result = b'HTTP/1.1 200 OK\r\n\r\nHello World!'
        #client_sock.sendall(data)
        client_sock.send(result)
        client_sock.close()
        break

    #client_sock.close()
