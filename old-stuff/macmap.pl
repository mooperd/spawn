#  macmap.pl
#  
#
#  Created by Iben Rodriguez on 10/26/13.
#
# begin - Iben Rodriguez
$SWIMLANE_ID = 1; # a number from 1-256 00-ff
$SWIMLANE_COUNT = 2; # How many swimlanes to configure?
$HYPERVISOR_ID = 1; # a number from 1-40
$HYPERVISOR_COUNT = 3; # How many Hypervisors per swimlane
# MAC Address
$OUI = "XX-XX-XX"; # Octets 1, 2, and 3
$MAC_TYPE_ID = 0; # Octet 4
$MAC_SWIMLANE_ID = 0; # Octet 5
$VM_ID = 0; # Octet 6
$VM_COUNT = 4; # How many VMs per hypervisor?
# IP Address
$IP_BASE = "192.168"; # Octets 1 and 2
$IP_SWIMLANE_ID = 0; # Octet 3
# Setup System variables
$now_string = localtime;  # e.g., " Mon Oct 21 15:25:14 2013."
print "Begin - $now_string.\n";
$row = 1;
$ge1 = 1;
$ge2 = 1;
$ge3 = 1;
$te1 = 1;
$te2 = 1;
print "VCT Virtual Swimlane to VM MAC and IP mapping\n";
print "SwimLane,Hypervisor,VM,MAC,IP\n";
for ($SWIMLANE_ID = 1; $SWIMLANE_ID <= $SWIMLANE_COUNT; $SWIMLANE_ID++) {
    for ($HYPERVISOR_ID = 1; $HYPERVISOR_ID <= $HYPERVISOR_COUNT; $HYPERVISOR_ID++) {
        for ($VM_ID = 1;$VM_ID <= $VM_COUNT; $VM_ID++) {
            printf ("%04d S%02XH%02XV%02X",$row,$SWIMLANE_ID,$HYPERVISOR_ID,$VM_ID);$row++;
            print ", $OUI-";
            $IP = ($HYPERVISOR_ID-1) * 10 + $VM_ID;
            printf ("%02X-%02X-%02X",$MAC_TYPE_ID,$SWIMLANE_ID,$IP);
            print ", $IP_BASE.$SWIMLANE_ID.$IP\n";
        }
    }
}
$now_string = localtime;
print "Done - $now_string.\n";
# end