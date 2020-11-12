#!/usr/bin/python3
import os
from prometheus_client import CollectorRegistry, Info, push_to_gateway

ipv4 = os.popen('ip addr show eth0').read().split("inet ")[1].split("/")[0]
ipv6 = os.popen('ip addr show eth0').read().split("inet6 ")[1].split("/")[0]

registry = CollectorRegistry()

i = Info('network_interfaces', 'Network Info', registry=registry)
i.info({'interface': 'eth0', 'address_v4': ipv4, 'address_v6': ipv6})
push_to_gateway('127.0.0.1:9091', job='network_info', registry=registry) 

