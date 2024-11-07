import psutil

def get_listening_ports():
    s = ""
    for cn in psutil.net_connections():
        if cn.status == psutil.CONN_LISTEN:
            s += "Port:"
            s += str(cn.laddr.port)
            s += " PID:"
            p = psutil.Process(cn.pid)
            s += str(p.pid)
            s += " Process Name: "
            s += p.name()
            s += "\n"
    return s

print(get_listening_ports())