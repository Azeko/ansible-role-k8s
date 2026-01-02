#!/usr/bin/python3
import sys
from haproxyadmin import haproxy
hap = haproxy.HAProxy(socket_dir='/run/haproxy')
servers = hap.servers()
s_len = len(servers)
down_list = []
for s in servers:
    if s.status == "DOWN":
        down_list.append(f"{s.name}, ")

down_len = len(down_list)
if down_len == 0:
    print("OK")
    sys.exit(0)

message = f"{down_len}/{s_len} api down\n"
for down_obj in down_list:
    message += down_obj


if down_len == s_len:
    print(f"CRITICAL: {message}")
    sys.exit(2)
else:
    print("WARNING: {message}")
    sys.exit(1)
