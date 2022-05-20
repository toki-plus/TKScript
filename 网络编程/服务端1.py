import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',8888))
server_socket.listen(5)
print('服务端开启监听...')
(new_socket, addr) = server_socket.accept()

print('客户端地址：', addr)
msg = '你好，我是服务端'
new_socket.send(msg.encode())

new_socket.close()
server_socket.close()
