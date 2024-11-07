import os
import datetime
import time

def ping(host):
    response = os.system(f"ping -c 2 {host}")
    return response == 0

def monit_netw(hosts):
    for host in hosts:
        if ping(host):
            print(f"{datetime.datetime.now()} | Host: {host} is available now")
        else:
            print(f"{datetime.datetime.now()} | Host: {host} is not available now")
if __name__ == "__main__":
    hosts = ["8.8.8.8", "google.com"]

    while True:
        monit_netw(hosts)
        time.sleep(30)