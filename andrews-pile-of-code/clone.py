#!/usr/bin/python
import sys, re, getpass, argparse, subprocess
from time import sleep
from pysphere import MORTypes, VIServer, VITask, VIProperty, VIMor, VIException
from pysphere.vi_virtual_machine import VIVirtualMachine

server = str('ESX')
username = 'root'
password = '1Qazxsw@'
template_vm = 'bang'

# Connecting to server
server = VIServer()
server.connect(server, username, password)
print ('Connected to server %s' % server)
print ('Server type: %s' % con.get_server_type())
print ('API version: %s' % con.get_api_version())

vm1 = server.get_vm_by_name("bang")
new_vm = vm1.clone("fuck-yeah")

