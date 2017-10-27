def censor(text, word):
  lst = text.split()
  new = []
  for item in lst:
    if item != word:
      new.append(item)
    else:
      censored = "*" * len(item)
      new.append(censored)
  return " ".join(new)
