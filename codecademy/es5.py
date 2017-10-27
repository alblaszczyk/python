grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for i in scores:
    total += i
  return total

print grades_sum(grades)

def grades_average(grades_input):
  avg_grds = grades_sum(grades_input) / float(len(grades_input))
  return avg_grds
print grades_average(grades)
