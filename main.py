val = '1'
try: 
    val=int(val)
except ValueError:
    print(f'val {val} is not a number')
else:
    print(val > 0)
finally:
    print("this will be printed no matter what")