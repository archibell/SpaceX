#
# Read the prefixes in the ip-ranges.json file and print them in the following format,
# which is grouped by region, then grouped by service, and then sorted by IP address:
#
# {
#   "<region>": {
#     "<service>": [
#       "<ip>", # sorted alphabetically
#       "<ip>",
#       "<ip>",
#       "<ip>"
#     ],
#     "<service>": [
#       "<ip>",
#       "<ip>",
#       "<ip>",
#       "<ip>"
#     ]
#   },
#   "<region>": ...
# }

from json import load, dumps
# load takes a file obj and returns the contents of the file as python objects (ie, a dict is a dict)
# dumps takes a json obj and returns a str with the json encoding that you can print.

with open("ip-ranges.json") as file:
  fileDict = load(file)
  resultDict = {}
  ipName = ""

  prefixList = fileDict["prefixes"]
  # print(prefixList[:4])
  for prefix in prefixList:
    regionStr = prefix["region"]
    serviceStr = prefix["service"]
    if "ip_prefix" in prefix:
      ipNameStr = "ip_prefix"
    else:
      ipNameStr = "ipv6_prefix"
    ipAddr = prefix[ipNameStr]

    if regionStr not in resultDict:
      resultDict[regionStr] = {}
    if serviceStr not in resultDict[regionStr]:
      resultDict[regionStr][serviceStr] = []

    resultDict[regionStr][serviceStr].append(ipAddr)

  for regionStr in resultDict:
    for serviceStr in resultDict[regionStr]:
      resultDict[regionStr][serviceStr].sort()

  print(dumps(resultDict, indent=4))
