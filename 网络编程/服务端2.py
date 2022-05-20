import socket
import threading

def recv(socket):
    while True:
        msg = socket.recv(1024)
        print('\n客户端说：', msg.decode())


def sent(socket):
    while True:
        msg = input('服务端输入：')
        socket.send(msg.encode())


server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',9999))
server_socket.listen(5)
print('服务端开启监听...')
(new_socket, addr) = server_socket.accept()

t_recv = threading.Thread(target=recv, args=(new_socket,))
t_sent = threading.Thread(target=sent, args=(new_socket,))

t_recv.start()
t_sent.start()