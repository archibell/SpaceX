#
# Write a program that parses the contents of the netstat.txt file and converts
# that information into YAML format and writes it to netstat.yaml.
#

import json
import yaml


def convertTxtYaml(file):
  with open(file) as f:
    resultDict = {}
    resultDict["Connections"] = []
    fileList = f.readlines()
    # print(fileList[:4])
    # ['Active Connections\n',
    # 'Proto  Local Address          Foreign Address        State\n',
    # 'TCP    0.0.0.0:135            0.0.0.0:0              LISTENING\n',...]
    for connection in fileList[2:]:
      connDict = {}
      connList = connection.split()
      # print(connList) # ['TCP', '0.0.0.0:135', '0.0.0.0:0', 'LISTENING']
      # ['UDP', '[::1]:54330', '*:*']
      proto = connList[0]
      localAddr = connList[1]
      colonInd = localAddr.rfind(":")
      localIP = localAddr[:colonInd]
      localPort = localAddr[colonInd + 1:]
      foreignAddr = connList[2]
      fcolonInd = foreignAddr.rfind(":")
      foreignIP = foreignAddr[:fcolonInd]
      foreignPort = foreignAddr[fcolonInd + 1:]
      connDict = {
          "Proto": proto,
          "LocalIP": localIP,
          "LocalPort": localPort,
          "ForeignIP": foreignIP,
          "ForeignPort": foreignPort
      }
      if proto == "TCP":
        state = connList[3]
        connDict["State"] = state
      # print(f"connDict: {connDict}")
      # connDict: {'Proto': 'TCP', 'LocalIP': '0.0.0.0', 'LocalPort': '135', 'ForeignIP': '0.0.0.0', 'ForeignPort': '0', 'state': 'LISTENING'}
      resultDict["Connections"].append(connDict)
    # print(json.dumps(resultDict, indent=4))
    outputFile = "netstat.yaml"
    with open(outputFile, "w") as o:
      yaml.dump(resultDict, o)


# Call the function to start.
file = "netstat.txt"
convertTxtYaml(file)

# Active Connections
# Proto  Local Address          Foreign Address        State
# TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
# TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
# UDP    [::1]:5353             *:*
# UDP    [::1]:54330            *:*
# UDP    [fe80::456b:b8c4:6165:6b53%16]:1900  *:*
