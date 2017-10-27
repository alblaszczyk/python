n = [3, 5, 7]

def total(numbers):
  result = 0
  for i in numbers:
    result += i
  return result

def total2(numbers):
  result = 0
  for i in range(len(numbers)):
    result += i
  return result
