#!/usr/bin/env python

from pysphere import VIServer

server = VIServer()
server.connect("10.51.3.59", "root", "1Qazxsw@")

vm = server.get_vm_by_path("[datastore 10.51.3.59-local] cheese01/cheese01.vmx")
print server.get_server_type()
vmlist = server.get_registered_vms()
print vmlist
vm = server.get_vm_by_path("[datastore 10.51.3.59-local] cheese01/cheese01.vmx")
vm.power_on()
