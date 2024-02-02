def factorial(n):
    if n <= 1:
        print(f"factorial({n}) = 1")
        return 1
    else:
        result = n * factorial(n - 1)
        print(f"factorial({n}) = {result}")
        return result
factorial(5) 

