# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words
# that are longer than n.

list = ["mark", "testing", "pitch", "darkness", "figures"]

def filter_long_words(list, n):
  for i in list:
    if len(i) > n:
      return i

print filter_long_words(list, 6)
