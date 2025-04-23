#
# Using the information in the ip-ranges.json list, print the Amazon service that
# has presence in the most number of unique regions (excluding the pseudo-service
# called "AMAZON").
#

from json import load, dumps
with open("ip-ranges.json") as f:
  jsonDict = load(f)
  prefixList = jsonDict["prefixes"]
  result = {}
  for prefix in prefixList:
    #     {
    #       "ip_prefix": "3.4.12.4/32",
    #       "region": "eu-west-1",
    #       "service": "AMAZON",
    #       "network_border_group": "eu-west-1"
    #     }
    serviceName = prefix["service"]
    regionName = prefix["region"]
    if serviceName != "AMAZON":
      if serviceName not in result:
        result[serviceName] = set()
      result[serviceName].add(regionName)
  # print(result)
  serviceCountList = [(serviceName, len(regions))
                      for serviceName, regions in result.items()]
  # print(serviceCountList)
  serviceCountList.sort(key=lambda c: c[1])
  print(serviceCountList[-1])

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
#       "ip_prefix": "3.209.85.0/25",
#       "region": "us-east-1",
#       "service": "ROUTE53_RESOLVER",
#       "network_border_group": "us-east-1"
#     },[]
