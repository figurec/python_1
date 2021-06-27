import os
import socket

port = int(os.environ.get("PORT", 5000))
print("PORT: ", port)

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
        data = client_sock.recv(1024)
        #if not data:
            # Клиент отключился
            #break
        #client_sock.sendall(data)
        client_sock.send('HTTP/1.1 200 OK\r\n\r\nHello World!')
        client_sock.close()

    #client_sock.close()
