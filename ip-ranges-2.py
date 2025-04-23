#
# Load the data in the ip-ranges.json file and print it in the same format but with the following changes:
#
# - Remove the IPv6 prefixes list altogether
# - Only keep prefixes in the "prefixes" list where the service is EC2
# - Sort the remaining prefixes by IP address
#

import json

# mylist = [
#   {
#     "name": "Victor"
#   },
# {
#     "name": "John"
#   }
# ]

# mylist.sort(key=lambda p: p["name"])
# print(mylist)

with open("ip-ranges.json") as f:
  jsonDict = json.load(f)  # Modify jsonDict in place.
  del jsonDict["ipv6_prefixes"]
  tempList = []  # Create a new list just for the prefixes.
  for prefixDict in jsonDict["prefixes"]:
    del prefixDict["network_border_group"]
    #     {
    #       "ip_prefix": "3.4.12.4/32",
    #       "region": "eu-west-1",
    #       "service": "AMAZON",
    #     },
    if prefixDict["service"] == "EC2":
      tempList.append(prefixDict)  # Append the original modified prefixDict.
  tempList.sort(key=lambda p: p["ip_prefix"])
  jsonDict[
      "prefixes"] = tempList  # Swap the existing prefixes list with the tempList.
  print(json.dumps(jsonDict, indent=4))

# INPUT

# {
#   "syncToken": "1742511196",
#   "createDate": "2025-03-20-22-53-16",
#   "prefixes": [
#     {
#       "ip_prefix": "3.4.12.4/32",
#       "region": "eu-west-1",
#       "service": "AMAZON",
#       "network_border_group": "eu-west-1"
#     },
#     {
#       "ip_prefix": "3.5.140.0/22",
#       "region": "ap-northeast-2",
#       "service": "EC2",
#       "network_border_group": "ap-northeast-2"
#     }
#   ],
#   "ipv6_prefixes": [
#     {
#       "ipv6_prefix": "3.5.140.0/22",
#       "region": "ap-northeast-2",
#       "service": "EC2",
#       "network_border_group": "ap-northeast-2"
#     }
#   ]
# }

# OUTPUT:

# {
#   "syncToken": "1742511196",
#   "createDate": "2025-03-20-22-53-16",
#   "prefixes": [
#     {
#       "ip_prefix": "3.4.12.4/32",
#       "region": "eu-west-1",
#       "service": "EC2"
#     }
#   ]
# }
