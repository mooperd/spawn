# cat -n clone_VMs_from_template_VM.py
     1  #!/usr/bin/env python
     2
     3  import sys
     4  import optparse
     5  from pysphere import VIServer
     6
     7  parser = optparse.OptionParser()
     8  parser.add_option('--prefix',type='string')
     9  parser.add_option('--number',type='int')
    10  parser.add_option('--template',type='string')
    11  parser.add_option('--vcenter',type='string')
    12  parser.add_option('--user',type='string')
    13  parser.add_option('--password',type='string')
    14  options, args = parser.parse_args()
    15
    16  opt_prefix = options.prefix
    17  opt_number = options.number
    18  opt_template = options.template
    19  opt_vcenter = options.vcenter
    20  opt_user = options.user
    21  opt_password = options.password
    22
    23  argvs = sys.argv
    24  argc = len(argvs)
    25
    26  if ( argc != 7):
    27          print "Usage : python clone_VMs_from_template_VM.py --vcenter=<vCenter IP> --user=<user> --password=<password>--prefix=<string> --number=<int> --template=<template VM name>"
    28          sys.exit(1)
    29
    30  # connect to vCenter
    31  server = VIServer()
    32  server.connect(opt_vcenter,opt_user,opt_password,trace_file="debug.txt")
    33
    34
    35  resource_pools = server.get_resource_pools()
    36  #print resource_pools
    37
    38  first_resource_pool = resource_pools.keys()[0]
    39  #print first_resource_pool
    40
    41  # specify the full path of a template VM
    42  template_vm = server.get_vm_by_name("%s" % opt_template)
    43
    44  i = 1
    45  while i <= opt_number:
    46          new_vm = "%s-%s" % ( opt_prefix,i )
    47          clonedVM = template_vm.clone(new_vm,resourcepool=first_resource_pool)
    48          print "VM name : %s : status %s" % (clonedVM.get_property("name") , clonedVM.get_status())
    49          i += 1
    50
    51  server.disconnect()
    53          i += 1
    54
    55  server.disconnect()
