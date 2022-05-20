import socket
import threading

def recv(socket):
    while True:
        msg = socket.recv(1024)
        print('\n服务端说：', msg.decode())


def sent(socket):
    while True:
        msg = input('客户端输入：')
        socket.send(msg.encode())


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9999))

t_recv = threading.Thread(target=recv, args=(client_socket,))
t_sent = threading.Thread(target=sent, args=(client_socket,))

t_recv.start()
t_sent.start()
