import psutil
import os

def save_data(data):
    with open(filename, "a+") as file:
        file.seek(0, 2)
        file.write(data + "\n")

def get_listening_ports():
    listening_ports = []
    for cn in psutil.net_connections():
        if cn.status == psutil.CONN_LISTEN:
            listening_ports.append(cn.laddr.port)
    return listening_ports

ports = get_listening_ports()
filename = "data.txt"

for port in ports:
    for con in psutil.net_connections():
        if con.status == psutil.CONN_LISTEN:
            p = psutil.Process(con.pid)
    data = f"Port: {port}  PID: {p.pid}  Process Name: {p.name()}"
    print(f"Port: {port}  PID: {p.pid}  Process Name: {p.name()}")
    save_data(data)