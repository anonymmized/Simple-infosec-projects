import psutil

def get_listening_ports():
    listening_ports = []
    for cn in psutil.net_connections():
        if cn.status == psutil.CONN_LISTEN:
            listening_ports.append(cn.laddr.port)
    return listening_ports

ports = get_listening_ports()
for port in ports:
    for con in psutil.net_connections():
        if con.status == psutil.CONN_LISTEN:
            p = psutil.Process(con.pid)
    print(f"Port: {port}  PID: {p.pid}  Process Name: {p.name()}")