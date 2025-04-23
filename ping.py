#
# Load the data from ping.txt and print the minimum, maximum, and average ping time.
#

min = float("inf")
max = float("-inf")
with open("ping.txt") as f:
  pingList = f.readlines()
  # print(pingList)
  timeList = []
  for pingStr in pingList:
    if "64 bytes" in pingStr:
      index = pingStr.rfind("=")
      # print(index)
      time = float(pingStr[index + 1:-3])
      # print(time)
      timeList.append(time)
      if time < min:
        min = time
      if time > max:
        max = time
  ave = sum(timeList) / len(timeList)
  print(min, ave, max)

# PING google.com (142.250.68.46) 56(84) bytes of data.
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=1 ttl=57 time=3.15 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=2 ttl=57 time=2.96 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=3 ttl=57 time=3.08 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=4 ttl=57 time=2.97 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=5 ttl=57 time=3.08 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=6 ttl=57 time=2.93 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=7 ttl=57 time=2.94 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=8 ttl=57 time=2.97 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=9 ttl=57 time=2.82 ms
# 64 bytes from lax17s46-in-f14.1e100.net (142.250.68.46): icmp_seq=10 ttl=57 time=2.88 ms

# --- google.com ping statistics ---
# 10 packets transmitted, 10 received, 0% packet loss, time 9408ms
# rtt min/avg/max/mdev = 2.817/2.977/3.145/0.093 ms

# with open("ping.txt") as f:
#   pingList = f.readlines()
#   # print(pingList)
#   timeList = []
#   for pingStr in pingList:
#     if "64 bytes" in pingStr:
#       index = pingStr.rfind("=")
#       # print(index)
#       time = float(pingStr[index + 1:-3])
#       # print(time)
#       timeList.append(time)
#   timeList.sort()
#   # print(timeList)
#   min = timeList[0]
#   max = timeList[-1]
#   ave = sum(timeList)/len(timeList)
#   print(min, ave, max)
