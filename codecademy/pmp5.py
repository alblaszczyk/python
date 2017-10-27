def factorial(x):
  count = 1
  stuff = 1
  while count <= x:
    stuff = stuff * count
    count = count + 1
  return stuff

print factorial(9)
