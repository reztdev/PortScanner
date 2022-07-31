#!/usr/bin/python3

import sys
if sys.version_info < (3, 0):
    sys.stdout.write("Please required python 3.x for run this tools\nAnd install nmap tools.")
    sys.exit(0)
import argparse
import socket
import time

try:
    import nmap
except ImportError:
    print("[!] Please install the modules nmap!! (pip install python-nmap)")
    exit(0)

class Color:
    W = '\033[0m'
    R = '\033[1;31m'
    G = '\033[1;32m'
    Y = '\033[1;33m'

def config_scan(target_host, target_port):
    try:
        target_ip = socket.gethostbyname(target_host)
        pyscan = nmap.PortScanner()
        pyscan.scan(target_host, target_port)
        state = pyscan[target_ip]['tcp'][int(target_port)]['state']
        if state == "closed":
            print("[{f}-{s}] {host} ({ip}) {port} {state}".format(
                f=Color.Y, s=Color.W, host=target_host, ip=target_ip, port=target_port, state=state
            ))
        else:
            print("[{f}+{s}] {host} ({ip}) {port} {state}".format(
                f=Color.G, s=Color.W, host=target_host, ip=target_ip, port=target_port, state=state
            ))
    except KeyboardInterrupt:
        print("[{f}!{s}] Interrupt by user, Exiting...".format(f=Color.R, s=Color.W))
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog=sys.argv[0], description="Simple Port Scanner with Nmap version 1.0",
            usage="%(prog)s -s [HOST] -p [PORT <separated by comma>]",
            formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=75, width=80),
            epilog="Copyright (c) ReztDev 2018. All right reserved")
    parser.add_argument("-s", "--host", dest="hostname", help="specify target host")
    parser.add_argument("-p", "--port", dest="port", help="specify target port[s] separated by comma (ex: 80,21,443)")
    options = parser.parse_args()
    port_scan = str(options.port).split(",")
    if (options.hostname == None) | (options.port == None):
        parser.print_help()
        exit(0)
    else:
        start = time.time()
        print("\n[{f}+{s}] Starting Port Scanner at {times}".format(
            f=Color.G, s=Color.W, times=time.strftime("%H:%M:%S-%p")
        ))
        for port_target in port_scan:
            config_scan(options.hostname, port_target)
        end = time.time()
        print("-" * 10)
        print("[{f}+{s}] Time elapsed: {total} seconds".format(
            f=Color.G, s=Color.W, total=round(end-start)
        ))
        print("[{f}+{s}] Scanning Completed.".format(f=Color.G, s=Color.W))

if __name__ == '__main__':
    main()
