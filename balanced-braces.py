#
# Given a string that contains square brackets, curly braces, and parentheses (collectively
# called "braces") write a function that returns whether the braces are correctly balanced.
# Braces are correctly balanced if for each opening brace of a particular kind there is a
# corresponding closing brace of the same kind, and the braces are also nested correctly.
#
# Braces = []{}()
#
# EXAMPLES
#
# [({})] = True
# ()()[[]] = True
#
# [{] = False
# [{]} = False
# [ = False


def balanced_braces(input: str) -> bool:
  dict = {")": "(", "]": "[", "}": "{"}
  stack = []
  for c in input:
    if c not in dict:  # Then I found a opening bracket.
      stack.append(c)
    # Otherwise, found a closing bracket.
    elif len(stack) == 0:
      return False
    else:
      openBracket = dict[c]
      print(openBracket)
      if stack.pop(-1) != openBracket:
        print("False")
        return False
  return not stack


input = "()()[[]]"
result = balanced_braces(input)
print(result)
