def remove_duplicates(lst):
  bonus_lst = []
  count = 0
  print lst
  for i in lst:
    if i not in bonus_lst:
      bonus_lst.append(i)
  return bonus_lst
