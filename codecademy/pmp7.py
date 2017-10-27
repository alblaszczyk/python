def reverse(text):listified = []
  reversing = []
  final_form = ''
  count = 1
  for letter in text:
    listified.append(letter)
  while count < len(listified):
    for letter in listified:
    	reversing.append(listified[len(listified) - count])
    	count += 1
  for letter in reversing:
    final_form += letter
  return final_form
