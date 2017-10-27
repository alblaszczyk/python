def median(lst):
  slst = sorted(lst)
  if len(slst) % 2 == 0:
    half1 = (len(slst)/2)
    half2 = (len(slst)/2) - 1
    print slst[half1]
    print slst[half2]
    return (slst[half1] + slst[half2])/2.0
  else:
    half = len(slst)/2
  return slst[half]

print median([1, 34, 1, 6, 8, 0])
