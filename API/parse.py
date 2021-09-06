#!/usr/bin/python3
import json

json_result = """
{
  "jsonrpc": "2.0",
  "id": "EapiExplorer-1",
  "result": [
    {
      "interfaces": {
        "Management0": {
          "name": "Management0",
          "interfaceStatus": "connected",
          "interfaceAddress": {
            "ipAddr": {
              "maskLen": 24,
              "address": "192.168.0.21"
            }
          },
          "ipv4Routable240": false,
          "lineProtocolStatus": "up",
          "mtu": 1500
        },
        "Ethernet2": {
          "name": "Ethernet2",
          "interfaceStatus": "connected",
          "interfaceAddress": {
            "ipAddr": {
              "maskLen": 24,
              "address": "2.2.2.2"
            }
          },
          "ipv4Routable240": false,
          "lineProtocolStatus": "up",
          "mtu": 1500
        },
        "Ethernet3": {
          "name": "Ethernet3",
          "interfaceStatus": "connected",
          "interfaceAddress": {
            "ipAddr": {
              "maskLen": 24,
              "address": "3.3.3.3"
            }
          },
          "ipv4Routable240": false,
          "lineProtocolStatus": "up",
          "mtu": 1500
        },
        "Ethernet1": {
          "name": "Ethernet1",
          "interfaceStatus": "connected",
          "interfaceAddress": {
            "ipAddr": {
              "maskLen": 24,
              "address": "1.1.1.1"
            }
          },
          "ipv4Routable240": false,
          "lineProtocolStatus": "up",
          "mtu": 1500
        },
        "Ethernet4": {
          "name": "Ethernet4",
          "interfaceStatus": "connected",
          "interfaceAddress": {
            "ipAddr": {
              "maskLen": 24,
              "address": "4.4.4.4"
            }
          },
          "ipv4Routable240": false,
          "lineProtocolStatus": "up",
          "mtu": 1500
        }
      }
    }
  ]
}
"""
sh_ip = json.loads(json_result)

for interface in sh_ip['result'][0]['interfaces']:
    ip = sh_ip['result'][0]['interfaces'][interface]['interfaceAddress']['ipAddr']['address']
    print(interface + ':', ip)


