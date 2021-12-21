#get ios and interfaces details
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72','carlo','cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces()
print (json.dumps(ios_output,sort_keys=True, indent=4))

ios_output = iosvl2.get_interfaces_counters()
print (json.dumps(ios_output, sort_keys=True, indent=4))


#get mac address table and arp table details and ping sample
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72','carlo','cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_arp_table()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.ping('google.com')
print (json.dumps(ios_output, indent=4))


#get bgp info1
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'carlo', 'cisco')
iosvl2.open()

bgp_neighbors = iosvl2.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

iosvl2.close()

#get bgp info2
import json
from napalm import get_network_driver

bgplist = ['192.168.122.72',
           '192.168.122.62'
           ]
for ip_address in bgplist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'carlo', 'cisco')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    iosv_router.close()


#configure access-lists
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'carlo', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.72')
iosvl2.load_merge_candidate(filename='ACL1.cfg')
iosvl2.commit_config()
iosvl2.close()

#compare configs
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'carlo', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.72')
iosvl2.load_merge_candidate(filename='ACL1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No changes required.')
    iosvl2.discard_config()

iosvl2.close()

#compare configs and audit
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'carlo', 'cisco')
iosvl2.open()

print ('Accessing 192.168.122.72')
iosvl2.load_merge_candidate(filename='ACL1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No ACL changes required.')
    iosvl2.discard_config()

iosvl2.load_merge_candidate(filename='ospf1.cfg')

diffs = iosvl2.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosvl2.commit_config()
else:
    print('No OSPF changes required.')
    iosvl2.discard_config()

iosvl2.close()


#multiple config files
import json
from napalm import get_network_driver

devicelist = ['192.168.122.72',
              '192.168.122.73'
             ]

for ip_address in devicelist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'carlo', 'cisco')
    iosv.open()
    iosv.load_merge_candidate(filename='ACL1.cfg')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required.')
        iosv.discard_config()

    iosv.load_merge_candidate(filename='ospf1.cfg')

    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
    	print('No OSPF changes required.')
    	iosv.discard_config()

    iosv.close()