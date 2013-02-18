#!/usr/bin/env python

import json
import socket
import os
import paramiko
import ping
import sys
import time

from config import hosts, op_timeout

# Checkers
##########

class ServiceChecker:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def do():
        return False

class PortServiceChecker(ServiceChecker):
    def __init__(self, host, port):
        ServiceChecker.__init__(self, host, port)

    def do(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(op_timeout)
        try:
            s.connect((self.host, self.port))
        except:
            return False
        return True

class SSHServiceChecker(ServiceChecker):
    def __init__(self, host, port, key):
        ServiceChecker.__init__(self, host, port)
        self.key = key

    def do(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(op_timeout)
        try:
            s.connect((self.host, self.port))
        except:
            return False
        t = paramiko.Transport(s)
        t.start_client()
        k = t.get_remote_server_key().get_base64()
        return k == self.key

# Generator
###########

def gen_json(outfile):
    output = []

    for h in hosts:
        lost, _, rtt = ping.quiet_ping(h["hostname"])

        status = lost is not 100

        services = []
        for s in h["services"]:
            if s["type"] == "port":
                c = PortServiceChecker(h["hostname"], s["port"]) 
            elif s["type"] == "ssh":
                c = SSHServiceChecker(h["hostname"], s["port"], s["key"])
            s_up = c.do()
            services += [{ "name": s["name"], "up": s_up }]
            if not s_up:
                status = False

        output += [{
            "hostname": h["hostname"],
            "status": status,
            "latency": rtt,
            "services": services,
        }]

    open(outfile, "w+").write(json.dumps(output))

if __name__ == "__main__":
    while True:
        gen_json(sys.argv[1])
        if len(sys.argv) > 2:
            time.sleep(int(sys.argv[2]))
        else:
            sys.exit(0)
