#
# Write a program that loads a list of connections from netstat.yaml and a filter
# from netstat-filter.yaml, applies the filter to the list of connections so that
# it only includes connections that match the specified values in the filter, and
# returns the new list of connections. Then use the Jinja template in netstat-template.j2
# to output the filtered list of connections in a textual format that resembles what
# the netstat tool prints.
#

import jinja2
import yaml

def applyFilterToNetstat(netstatFile, filterFile):
  filtersKV = []
  result = {}
  result["Connections"] = []
  with open(filterFile) as filterF:
    filterDict = yaml.safe_load(filterF)
    filters = filterDict["filter"]
    for filterName, filterValue in filters.items():
      filtersKV.append((filterName, filterValue))
    # print(filtersKV) # [('Proto', 'TCP'), ('ForeignIP', '54.187.159.182')]

  with open(netstatFile) as f:
    netDict = yaml.safe_load(f)
    connList = netDict["Connections"]
    # print(connList[:3])
    # [{'ForeignIP': '0.0.0.0', 'ForeignPort': '0', 'LocalIP': '0.0.0.0', 'LocalPort': '135', 'Proto': 'TCP', 'State': 'LISTENING'},]
    for conn in connList:
      if checkFilterOnConn(conn, filtersKV):
        result["Connections"].append(checkFilterOnConn(conn, filtersKV))
  return result

def checkFilterOnConn(conn, filtersKV):  # -> List[str]
  for filterName, filterValue in filtersKV:
    if filterName not in conn:
      return
    if conn[filterName] != filterValue:
      return
  return conn

netstatFile = "netstat.yaml"
filterFile = "netstat-filter.yaml"
solution = applyFilterToNetstat(netstatFile, filterFile)
# print(yaml.dump(solution))

with open("netstat-template.j2") as f:
  template = jinja2.Template(f.read())  # template.render(obj)
  print(template.render(solution))

# filter:
#   Proto: "TCP"
#   ForeignIP: "54.187.159.182"

# filter:
#   LocalPort: "443"
#   State: "TIME_WAIT"

# filter:
#   Proto: "UDP"
