#!/usr/bin/python3
import os
from prometheus_client import CollectorRegistry, Info, push_to_gateway

ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
print(ipv4)

ip = os.popen('ip addr show').read()
print(ipv4)

# registry = CollectorRegistry()

# i = Info('network_interfaces', 'Network Info', registry=registry)
# i.info({'interface': 'eth0', 'address_v4': ipv4})
# push_to_gateway('127.0.0.1:9091', job='network_info', registry=registry) 

