#
# Write a function that parses an IPv4 address and returns the corresponding
# 32-bit number that represents that address.
#
# IPv4:
# - 10.0.0.1    = 0b 00001010 00000000 00000000 00000001 = 1*2**0 + 0*2**8 + 0*2**16 + 10*2**24
# - 192.168.0.2 = 0b 11000000 10101000 00000000 00000010
# - 1.1.1.1     = 0b 00000001 00000001 00000001 00000001
#
# 10 << 24 = 0b 00001010 00000000 00000000 00000000
#  0 << 16 = 0b          00000000 00000000 00000000
#  0 << 8  = 0b                   00000000 00000000
#  1 << 0  = 0b                            00000001
#
# NOT:  ~0b11110000 = 0b00001111
# OR:    0b11110000 | 0b00001111 = 0b11111111 (also |=)
# AND:   0b11110000 & 0b00111111 = 0b00110000 (also &=)
# SHIFT: 0b00001111 << 2 = 0b00111100 (also <<=)
# SHIFT: 0b00001111 >> 3 = 0b00000001 (also >>=)
#


def parsingIPv4Addr(input):
  # PARSE IP ADDRESSES USING BITWISE OR "|" AND SHIFT LEFT "<<".
  result = 0
  octetList = input.split(".")
  # print(octetList) # ['10', '0', '0', '1']
  n = 24  # Starting location for the 1st octet.
  for octet in octetList:
    # print(f"n:{n}, octet: {octet}") # octet = '10', or a decimal number.
    result |= int(octet) << n  # Place the octet in it's final location using Bitwise shift left.
    # And added to the result using Bitwise OR operation.
    n -= 8  # Decrement 8 bits for every octet processed.
  return result

# Call to function below:
input = "192.168.0.2"
solution = parsingIPv4Addr(input)
print(f"parsingIPv4Addr: {bin(solution)}")
# Expected: parsingIPv4Addr: 0b11000000101010000000000000000010

#==================================================================================================

#
# Write a function that parses an IPv6 address and returns the corresponding
# 128-bit number that represents that address. This function must support
# IPv6 address shortening (::) where a run of 0000 groups in the middle of the
# address is removed to make the address shorter.
#
# IPv6:
# - 2 (hexadecimal) = 0010 (bin) = 2 (dec)10
# - f (hexadecimal) = 1111 (bin) = 15 (dec)
# - 2001 (hexadecimal) = 0010 0000 0000 0001 (bin) = ??? (dec)
#
# - 2001:0db8:85a3:0000:0000:8a2e:0370:7334
# - 2001:db8:85a3::8a2e:370:7334 (same as: 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
# - 2c0f:c20a:12::1
#

def parsingIPv6Addr(input) -> int:
  # PARSE IP ADDRESSES USING BITWISE OR "|" AND SHIFT LEFT "<<".
  result = 0
  ipv6List = input.split(":")
  # print(f"ipv6List: {ipv6List}"
  # ipv6List: ['2001', 'db8', '85a3', '', '8a2e', '370', '7334']
  # Go forwards until find the shortened groups if any.
  i = 112
  for group in ipv6List:
    if group != "":
      # group = "0db8", which is a hexadecimal string number.
      result |= int(group, 16) << i
      i -= 16
    elif group == "":
      break  # Exits the loop completely.
  # Go backwards until find the shortened groups if any.
  j = 0
  for group in ipv6List[::-1]:  # "7334"
    if group != "":
      result |= int(group, 16) << j
      j += 16
    elif group == "":
      break
  print(f"parsingIPv6Addr result: {result}") # Decimal number: 42540766452641154071740215577757643572
  return result

# Call to function below:
input = "2001:db8:85a3::8a2e:370:7334"
solution = parsingIPv6Addr(input)
print(f"parsingIPv6Addr: {bin(solution)}")
# Expected: parsingIPv6Addr: 0b100000000000010000110110111000100001011010001100000000000000000000000000000000100010100010111000000011011100000111001100110100

#==================================================================================================

#
# Write a function that given a CIDR and an IPv4 address determines whether the IP
# address is part of the subnet represented by that CIDR.
#
# 10.0.0.0/8
# 1.2.3.15/28 = 00000001 00000010 00000011 0000|1111
# 1.2.3.0/28  = 00000001 00000010 00000011 0000|0000
# 1.2.3.17/28 = 00000001 00000010 00000011 0001|0001
# 1.2.3.16/28 = 00000001 00000010 00000011 0001|0000
# cidr = 1.2.3.16/28, ip = 1.2.3.22 = True
# cidr = 1.2.3.16/28, ip = 1.2.3.32 = False
#
# cidr = 10.125.166.0/24 -> 00001010 01111101 10100110 00000000
# ip   = 10.125.166.123  -> 00001010 01111101 10100110 01111011
# mask = ~0 << 8         -> 11111111 11111111 11111111 00000000
# Result: True
#
# cidr = 10.125.166.0/24 -> 00001010 01111101 10100110 00000000
# ip   = 10.125.167.1    -> 00001010 01111101 10100111 00000001
# mask = ~0 << 8         -> 11111111 11111111 11111111 00000000
# Result: False
#

def verifyCidrAllowed(cidr, ip) -> bool:
  # VERIFY IP ADDRESS WITHIN CIDR RANGE VIA BITWISE AND "&" WITH A MASK THAT
  # IS BUILT FROM ALL 1'S SHIFTED LEFT.
  cidrList = cidr.split("/")
  # print(cidrList) # ['10.125.166.0', '24']
  cIP, cNum = cidrList[0], int(cidrList[1])
  # print(f"cIP: {cIP}, cNum: {cNum}")
  cIPBin = parsingIPv4Addr(cIP) # Used helper function.
  # print(f"cIPBin: {cIPBin}") # 176006656
  ipBin = parsingIPv4Addr(ip) # Used helper function.
  # print(f"ipBin: {ipBin}") # 176006779

  shiftNum = 32 - cNum
  bitmask = ~0 << shiftNum
  maskedIP = ipBin & bitmask
  return cIPBin == maskedIP # Returns bool.

# Call to function below:
cidr = "10.125.166.0/24"
ip = "10.125.167.1"
solution = verifyCidrAllowed(cidr, ip)
print(solution) # Expected: False








