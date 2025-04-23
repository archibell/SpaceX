import json  # load, dumps

#
# Load the traceroute.json file and return the index of the hop with the highest worst latency.
#


def findWorstHop(fileName) -> int:
  with open(fileName) as file:
    trDict = json.load(file)
    hopsList = trDict["hops"]
    (index, worstTime) = (0, float("-inf"))
    for i, hop in enumerate(hopsList):
      if hop["host"] != "":  # I have a hop reply data.
        time = hop["pings"]["worst"]
        if time > worstTime:
          (index, worstTime) = (i, time)
    # print(f"index: {index}, worstTime: {worstTime}")
    return index


solution = findWorstHop("traceroute.json")
print(solution)  # Expected: 9

# ===================================================================

#
# Load the traceroute.json file and return the cumulative packet loss percentage across all hops.
#


def findAvePacketLoss(fileName) -> float:
  with open(fileName) as file:
    trDict = json.load(file)
    hopsList = trDict["hops"]
    lostPackets = 0
    totalPackets = 0
    for hop in hopsList:
      if hop["host"] != "":  # I have a hop reply data.
        sentPackets = hop["packets"]["sent"]
        totalPackets += sentPackets
        lossPercentage = hop["packets"]["loss"] / 100
        lostPackets += sentPackets * lossPercentage
    avePacketLoss = lostPackets / totalPackets
    # print(lostPackets, totalPackets, avePacketLoss)
    return avePacketLoss * 100


solution = findAvePacketLoss("traceroute.json")
print(solution)  # Expected: 3.5616438356164384

# ===================================================================

# Return a list of hosts, sorted first by packet loss descending (largest to smallest),
# then by number of packets sent descending,
# then finally by host name.


def sortTraceRouteHosts(fileName):
  with open(fileName) as file:
    trDict = json.load(file)
    hopsList = trDict["hops"]
    result = []
    for hop in hopsList:
      if hop["host"] != "":
        packetLoss = hop["packets"]["loss"]
        packetSent = hop["packets"]["sent"]
        hostName = hop["host"]
        result.append((-packetLoss, -packetSent, hostName))
    # print(result) # [(-12.5, -8, '172.23.144.1'), (-20.0, -8, '10.250.30.1'),...]
    result.sort()
    # print(result) # [(-20.0, -8, '10.250.30.1'), (-12.5, -8, '172.23.144.1'),...]
    result = [tuple[-1] for tuple in result]
    return result


solution = sortTraceRouteHosts("traceroute.json")
print(solution)
# Expected:
# ['10.250.30.1', '172.23.144.1', 'te-0-0-0-27-0-10.er01.lax01.riotdirect.net', '206.72.211.146.any2ix.coresite.com', '52.93.92.155', '52.93.92.33', '52.93.92.40', '52.93.92.49', 'a8e1d94f26b1cf33b.awsglobalaccelerator.com', 'ae1.er02.lax01.riotdirect.net']

# ===================================================================

# Return a list of hops, sorted first by packet loss descending (largest to smallest),
# then by number of packets sent descending,
# then finally by host name.


def sortTraceRouteHops(fileName):
  with open(fileName) as file:
    trDict = json.load(file)
    hopsList = trDict["hops"]
    result = []
    for hop in hopsList:
      if hop["host"] != "":
        result.append(hop)
    result.sort(key=lambda h:
                (-h["packets"]["loss"], -h["packets"]["sent"], h["host"]))
    return result


#
# The lambda h: ... expression above has the same effect as this function:
#
# def anonymousLambda1(h):
#     return (-h["packets"]["loss"], -h["packets"]["sent"], h["host"])

solution = sortTraceRouteHops("traceroute.json")
print(json.dumps(solution, indent=4))

# ===================================================================


def getHopSortKey(hop):
  packetLoss = hop["packets"]["loss"]
  packetSent = hop["packets"]["sent"]
  hostName = hop["host"]
  hopSortKey = (-packetLoss, -packetSent, hostName)
  return hopSortKey


def sortTraceRouteHops2(fileName):
  with open(fileName) as file:
    trDict = json.load(file)
    hopsList = trDict["hops"]
    result = []
    for hop in hopsList:
      if hop["host"] != "":
        result.append(hop)
    result.sort(key=getHopSortKey)
    return result


solution = sortTraceRouteHops2("traceroute.json")
print(json.dumps(solution, indent=4))
