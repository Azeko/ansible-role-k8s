#!/usr/bin/python3

import socket, sys, yaml

with open('/etc/check_sockets/check_sockets.yaml') as fh:
    ips_ports = yaml.safe_load(fh)

final = {}
def check_port(inter, ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((inter, 0))
        socket.setdefaulttimeout(2.0)
        result = sock.connect_ex((ip,port))
        if result == 0:
            final[ip][port] = "OPEN"
        else:
            final[ip][port] = "CLOSED"
        sock.close()
    except:
        final[ip] = "EXCEPTION"
        
  
def create_ip_port_dict(inter):
    for ip in ips_ports[inter].keys():
       final[ip] = {}
       for port in ips_ports[inter][ip]:
          if type(port) is str and ":" in port:
              ports = port.split(":")
              start_port = int(ports[0])
              end_port   = int(ports[1])
              while start_port <= end_port:
                check_port(inter, ip, start_port)
                start_port = start_port + 1
                
          else:    
              check_port(inter,ip,port)
                      
  
text = ""
for inter in ips_ports.keys():  
    create_ip_port_dict(inter) 
    for ip in final.keys():  
        for port in final[ip].keys():
            if final[ip][port] != "OPEN":
                text += f"{ip}:{port} "
                
if text != "":
        text = f"{socket.gethostname()} can't reach {text} "
        print(text)
        sys.exit(1)
else:
        text = f"for {socket.gethostname()} all sockets are reachable"
        print(text)
        sys.exit(0) 
