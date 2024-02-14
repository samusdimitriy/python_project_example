l1 = set(["red", "green", "blue"])
l2 = set(["yellow", "green", "blue"])
a = {"red"}

l3 = l1|l2 # union
l4 = l1&l2 # intersection
l5 = l1-l2 # difference
l6 = l2-l1 # difference
l7 = l1^l2 # symmetric difference
b = a.issubset(l2)

print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(b)