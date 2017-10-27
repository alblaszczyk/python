# Write your function below!
def fizz_count(x):
  count = 0
  for i in x:
    if i == "fizz":
    	count += 1
  return count
fizz_count(["fizz", "cat", "fizz"])
