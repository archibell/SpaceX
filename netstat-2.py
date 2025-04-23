#
# Read the contents of the netstat.txt file, which looks like the INPUT below.
# Then create the result as shown under OUTPUT, where the result is a JSON object
# where you first group by Protocol, then by Local Address (without port), and
# then list all of the connections from that local address formatted as shown.
#
# INPUT:
#
# TCP    0.0.0.0:49682          0.0.0.0:0              LISTENING
# TCP    0.0.0.0:60764          0.0.0.0:0              LISTENING
# TCP    10.250.20.28:139       0.0.0.0:0              LISTENING
# TCP    10.250.20.28:60766     142.250.72.142:443     TIME_WAIT
# TCP    10.250.20.28:60803     172.215.180.16:9354    ESTABLISHED
# TCP    10.250.20.28:60822     54.70.179.16:443       ESTABLISHED
#
# OUTPUT:
#
# {
#   "TCP": {
#     "0.0.0.0": [
#       {
#         "port": "49682",
#         "foreign": "0.0.0.0:0",
#         "state": "LISTENING"
#       },
#       {
#         "port": "60764",
#         "foreign": "0.0.0.0:0",
#         "state": "LISTENING"
#       }
#     ],
#     "10.250.20.28": [
#       {
#         "port": "139",
#         "foreign": "0.0.0.0:0",
#         "state": "LISTENING"
#       }
#     ]
#   },
#   "UDP": {
#     ...
#   }
# }

import json


def reformatNetstat(netstatFile):
  result = {}
  result["TCP"] = {}
  result["UDP"] = {}
  with open(netstatFile) as f:
    netstatList = f.readlines()[2:]
    # print(netstatList)
    for status in netstatList:
      status = status.split(
      )  # ['TCP', '0.0.0.0:135', '0.0.0.0:0', 'LISTENING']
      # print(status)
      proto = status[0]
      localIP = status[1]
      colonIndex = localIP.rfind(":")
      localAddr = localIP[:colonIndex]
      port = localIP[colonIndex + 1:]
      foreignIP = status[2]
      tempDict = {"port": port, "foreign": foreignIP}
      if proto == "TCP":
        state = status[3]
        tempDict["state"] = state
      # print(proto, localAddr, port, foreignIP, state) # TCP 0.0.0.0 445 0.0.0.0:0 LISTENING
      if localAddr not in result[proto]:
        result[proto][localAddr] = []
      result[proto][localAddr].append(tempDict)

  print(json.dumps(result, indent=4))  # {'TCP': {}, 'UDP': {}}


file = "netstat.txt"
reformatNetstat(file)
