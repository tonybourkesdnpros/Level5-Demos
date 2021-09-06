#!/usr/bin/python3

import pyeapi

switches = ['leaf1-DC1', 'leaf2-DC1', 'leaf3-DC1', 'leaf4-DC1']

# Create VLANs 1000-1999

for switch in switches: 
   connect = pyeapi.connect_to(switch) 
   for vlan in range(1000, 2000):
       print("vlan:", vlan)
       result = connect.api('vlans').create(vlan)
       if result == True:
          print("Completed!")

       if result == False:
          print("Error!")
