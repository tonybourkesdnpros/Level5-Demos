#!/usr/bin/python3

import pyeapi, yaml

# Open a session with leaf1-DC1 

interfaces_yml = open("interfaces.yml", "r")

interfaces = yaml.safe_load(interfaces_yml)


for switch in interfaces:
    connect = pyeapi.connect_to(switch)
    for interface in interfaces[switch]['interfaces']:
      connect.api("ipinterfaces").create(interface)
      ip = interfaces[switch]['interfaces'][interface]
      result = connect.api("ipinterfaces").set_address(interface,ip)
      if result == True:
        print("Completed!")

      if result == False:
        print("Error!")

