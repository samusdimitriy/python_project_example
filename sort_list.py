lst = [5,4,3,2,1]

def sort_list(data):
    return sorted(data)[1:-1]

# print(sort_list(lst)) # [2, 3, 4]

def amount_payment(payment):
    sum = 0
    for i in payment:
        if i >= 0:
            sum += i
    return sum 
        
    
print(amount_payment([1, -3, 4]))  

