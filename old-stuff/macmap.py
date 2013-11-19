#! /usr/bin/env python
#  macmap.py
#  Created by Iben Rodriguez on 10/27/13.
import time
import datetime
# setup system variables
# IP Address
IP_BASE = "192.168." # Octets 1 and 2 with dot delimiters
SWIMLANE_ID = 1 # a number from 1-40
SWIMLANE_COUNT = 1 # How many swimlanes to configure?
HYPERVISOR_ID = 1 # a number from 1-254
HYPERVISOR_COUNT = 1 # How many Hypervisors total
NUMBER_OF_HYPERVISORS_PER_SWIMLANE = 1
VM_COUNT = 127 # How many VMs per hypervisor?
OUI = "00:50:56" # MAC Address Octets 1, 2, and 3
MAC_TYPE_ID = 0 # Octet 4
row = 1
print "*** BEGIN JOB RUN = " + datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
print "OUI = ",(OUI)
print "VCT Virtual Swimlane to VM MAC and IP mapping"
print "Count, VM_NAME, VM_MAC, VM_IP"
while SWIMLANE_ID <= SWIMLANE_COUNT:
    while HYPERVISOR_ID <= HYPERVISOR_COUNT:
        HYP_COUNT = 1
        while HYP_COUNT <= NUMBER_OF_HYPERVISORS_PER_SWIMLANE:
            VM_ID = 1 # Octet 6
            HYP_COUNT += 1
            while VM_ID <= VM_COUNT:
                VMH = format(VM_ID, '02X')
                print "# row number " + (format(row,'04d'))
                print "host " + "S" + format(SWIMLANE_ID,'02d') + "H" + (format(HYPERVISOR_ID, '02d')) + "V" + (VMH) + ".vct.nsslabs.com {"
                print "hardware ethernet " + (OUI) + ":" + (format(MAC_TYPE_ID, '02x') + ":" + format((HYPERVISOR_ID),'02x') + ":" + (VMH)) + ";"
                print "fixed-address " + IP_BASE  + format(HYPERVISOR_ID,'d')  + "." + format(VM_ID,'d') + ";"
                print "option host-name \"" + "S" + format(SWIMLANE_ID,'02d') + "H" + (format(HYPERVISOR_ID, '02d')) + "V" + (VMH) + ".vct.nsslabs.com\";"
                print "filename \"pxelinux.0\";"
                    #
                row += 1
                VM_ID += 1
            HYPERVISOR_ID += 1
        SWIMLANE_ID += 1
print "*** END JOB RUN = " + datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
# example DHCP.CONF file from Andrew
# host node003.swim1.test.nsslabs.com {
# hardware ethernet 00:00:00:00:02:03;
# fixed-address 10.51.102.3;
# option host-name "node003.test.nsslabs.com";
# filename "pxelinux.0";
# }