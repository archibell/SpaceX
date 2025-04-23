#
# Using the templates in device-templates.yaml and the devices in devices.json,
# generate the desired list of devices, where each device starts with the data
# from its template and then modifies some of the attributes with custom values,
# leaving the other attributes that come from the template unchanged. Do not
# modify the original templates themselves.
#

import yaml
import json
with open("device-templates.yaml") as templatesF:
  with open("devices.json") as devicesF:
    templatesDict = yaml.safe_load(templatesF)
    templatesList = templatesDict["devices"]
    tempDict = {}  # This is the template dict I want to compare to later.
    for template in templatesList:
      tempDict[template["name"]] = template
    # print(json.dumps(tempDict, indent = 4))

    devicesDict = json.load(devicesF)
    result = {}
    result["devices"] = []
    devicesList = devicesDict["devices"]
    for device in devicesList:
      # {
      #   "template": "R1",
      #   "name": "R3",
      #   "bgpasn": "65002"
      # },
      deviceTemplateName = device["template"]
      template = tempDict[deviceTemplateName]
      modifiedTemplate = template.copy()
      del device["template"]  # Remove b/c no longer needed.
      for key, value in device.items():
        modifiedTemplate[key] = value
      result["devices"].append(modifiedTemplate)
    print(json.dumps(result, indent=4))

# TEMPLATES
#
# devices:
# - name: "R1"
#   interfaces:
#     - name: "Ethernet1/1"
#       state: "enabled"
#       ip: "10.0.0.1"
#       mask: "255.255.255.0"
#       qos_policy: "SHAPE_200MB"
#     - name: "Loopback0"
#       state: "enabled"
#       ip: "1.1.1.1"
#       mask: "255.255.255.255"
#   bgpasn: "65000"
#   bgp_neighbors:
#     - ip: "10.0.0.2"
#       remote_as: "65001"
# - name: "R2"
#   interfaces:
#     - name: "Ethernet1/1"
#       state: "enabled"
#       ip: "10.0.0.2"
#       mask: "255.255.255.0"
#       qos_policy: "SHAPE_200MB"
#   bgpasn: "65001"
#   bgp_neighbors:
#     - ip: "10.0.0.1"
#       remote_as: "65000"

# DEVICES
#
# {
#   "template": "R1",
#   "name": "R3",
#   "bgpasn": "65002"
# }

# OUTPUT
#
# {
#   "name": "R3",
#   "interfaces": [
#     {
#       "name": "Ethernet1/1",
#       "state": "enabled",
#       "ip": "10.0.0.1",
#       "mask": "255.255.255.0",
#       "qos_policy": "SHAPE_200MB"
#     },
#     {
#       "name": "Loopback0",
#       "state": "enabled",
#       "ip": "1.1.1.1",
#       "mask": "255.255.255.255"
#     }
#   ],
#   "bgpasn": "65002",
#   "bgp_neighbors": [
#     {
#       "ip": "10.0.0.2",
#       "remote_as": "65001"
#     }
#   ]
# }
