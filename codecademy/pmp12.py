def purify(lst):
  even_lst = []
  for num in lst:
    if num % 2 == 0:
      even_lst.append(num)
  return even_lst
