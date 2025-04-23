f = open("netstat.txt")

#
# Parse the netstat.txt file and print how many TCP connections are in each state
# (ESTABLISHED, TIME_WAIT, etc).
#


def parseNetStat(f):  # Print the number of TCP connections by state.
  lineList = f.readlines()
  # print(lineList)
  tcpDict = {}
  for str in lineList[2:]:
    statusList = str.split()
    # print(statusList)
    if statusList[0] == "TCP":
      if statusList[-1] in tcpDict:
        tcpDict[statusList[-1]] += 1
      else:
        tcpDict[statusList[-1]] = 1
  print(f"tcpDict: {tcpDict}")


parseNetStat(f)
f.close()

#
# Parse the netstat.txt file and print the foreign IP addresses that have the most connections
# to them, regardless of port.
#

f = open("netstat.txt")


def mostConnections(f):
  lineList = f.readlines()
  # print(lineList)
  foreignDict = {}
  result = []
  for str in lineList[2:]:
    statusList = str.split()
    colonInd = statusList[2].rfind(":")
    ipAddr = statusList[2][:colonInd]
    # print(ipAddr)
    if ipAddr in foreignDict:
      foreignDict[ipAddr] += 1
    else:
      foreignDict[ipAddr] = 1
  # print(foreignDict)
  for ipAddr, count in foreignDict.items():
    result.append((count, ipAddr))
  # print(result)
  result.sort()
  result.reverse()
  print(f"mostConnection: {result}")


mostConnections(f)
f.close()
