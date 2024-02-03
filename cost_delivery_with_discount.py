def cost_delivery(quantity, *_, discount = 0):
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result

print(cost_delivery(3,2,3,4))