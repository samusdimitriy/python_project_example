def cost_delivery(quantity, *numbers, discount = 0):
    cost_first_delivery = 5
    cost_sub_deliveries = 2

    sum_delivery = (quantity - 1) * cost_sub_deliveries + cost_first_delivery
    return sum_delivery * (1 - discount)

print(cost_delivery(1))