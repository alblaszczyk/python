shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(shopping_list):
    total = 0
    for i in shopping_list:
        if stock[i] > 0:
          total += prices[i]
          stock[i] -= 1
    return total
print compute_bill(shopping_list)
