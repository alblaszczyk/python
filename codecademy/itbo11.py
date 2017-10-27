def check_bit4(input):
  mask = 0b1000
  test = input & mask
  if test > 0:
    return "on"
  else:
    return "off"
    
