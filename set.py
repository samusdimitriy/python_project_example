# l1 = set(["red", "green", "blue"])
# l2 = set(["yellow", "green", "blue"])
# a = {"red"}

# l3 = l1|l2 # union
# l4 = l1&l2 # intersection
# l5 = l1-l2 # difference
# l6 = l2-l1 # difference
# l7 = l1^l2 # symmetric difference
# b = a.issubset(l2)

# print(l3)
# print(l4)
# print(l5)
# print(l6)
# print(l7)
# print(b)

cards = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "KS"]

def is_flush(cards):  
    suits = set([card[1] for card in cards])  
    return suits


