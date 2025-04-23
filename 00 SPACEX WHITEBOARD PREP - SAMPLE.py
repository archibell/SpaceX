# WHITEBOARD PREP - SAMPLE CODILITY TECH ASSESSMENT
# ===================================================================================================

# PYTHON OPEN() - READ/APPEND/WRITE/NEW FILE:
# ===================================================================================================
# "R" - OPEN, READ, & PARSE THE TXT FILE:
# ------------------------------------------------------------------------------
file = open("netstat.txt")  # Open the file.

def parseNetStat(file):  # Print the num of TCP connections by state.
    lineList = file.readlines()  # Read all lines into a list.
    # print(lineList[:3])  # For local testing only.
    # Ex: ['Active Connections\n',
    # 'Proto  Local Address          Foreign Address        State\n',
    # 'TCP    0.0.0.0:135            0.0.0.0:0              LISTENING\n']
    tcpDict = {}
    for str in lineList[2:]:  # Iterate thru each string in list, starting from 3rd row.
        statusList = str.strip().split()  # strip() - removes any leading and trailing white spaces from string.
        # split() - splits str at a specified separator, and returns a list.
        # print(statusList)     # For local testing only.
        #  ['TCP', '0.0.0.0:135', '0.0.0.0:0', 'LISTENING']
        if statusList[0] == "TCP":
            if statusList[-1] in tcpDict:
                tcpDict[statusList[-1]] += 1
            else:
                tcpDict[statusList[-1]] = 1
    print(f"tcpDict: {tcpDict}")

parseNetStat(file)  # Call to initiate function.
                    # Expected Answer: {'LISTENING': 52, 'TIME_WAIT': 10, 'ESTABLISHED': 117}
file.close()    # Whoever opens file, should close it.

# Using "with open("path_to_file", mode) as f" - will autoCLOSE file for you.
# "A" - OPEN EXISTING FILE, & APPEND TO FILE:
# ------------------------------------------------------------------------------
with open("TestOutput_PythonOpenA.txt", "a") as f:
    f.write("I opened with mode = 'a', append.\n")
    f.write("I am appending to this file.\n")
    f.write("\n")

with open("TestOutput_PythonOpenA.txt") as myFile:
    print(myFile.read())

# "W" - OPEN & WRITE (OVERWRITE) THE TXT FILE:
# ------------------------------------------------------------------------------
with open("TestOutput_PythonOpenW.txt", "w") as f:
    f.write("I opened with mode = 'w', overwrite.\n")
    f.write("I am overwriting this file.\n")

# "X" - OPEN, CREATE A NEW FILE, & WRITE TO FILE:
# ------------------------------------------------------------------------------
with open("TestOutput_PythonOpenX.txt", "x") as f:
    f.write("I opened with mode = 'x', new file.\n")
    f.write("I am writing to this file.\n")
    f.write("I will fail if file already exists.\n")
    # IMPORTANT: DELETE "TestInput_PythonOpenX.txt" IF RERUNNING THIS FILE.

# PYTHON JSON PACKAGE:
# ===================================================================================================
import json
# json.load(file obj)     # Takes a file object and returns the contents of the file as python objects
#                         # (ie, convert json to read as a python dict)
# json.loads(python str)  # Takes a string that contains json encoded data and
#                         #returns python objects that represent that data.

# json.dump(python obj, file, indent)   # Takes a python object (ex: dict/list/string/yaml)
#                                       # and converts to a json file.
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
with open("TestOutput_json_dump.json", "w") as f:
    json.dump(data, f, indent=4)

# json.dumps(python obj, indent)  # Takes a python object (ex: dict/list/string/yaml) and converts to a json string.

# ------------------------------------------------------------------------------
import json
with open("ip-ranges.json") as file:
  fileDict = json.load(file)
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

  print(f"TestOutput_json.dumps(): {json.dumps(resultDict, indent = 4)}")

# PYTHON YAML PACKAGE:
# ===================================================================================================
import yaml
# yaml.safe_load(file obj or python str)  # Takes a file object or a String
#                                         # and returns the contents of the file as python objects.

# yaml.dump(python obj)       # If pass in only python obj, it returns a string.
data = {
"name": "John Doe",
"age": 30,
"city": "New York"
}
yaml.dump(data)

# yaml.dump(python obj, file) # If pass in python obj and a file, then it writes to the file.
data = {
"name": "John Doe",
"age": 30,
"city": "New York"
}
with open("TestOutput_yaml_dump.yaml", "w") as f:
    yaml.dump(data, f)