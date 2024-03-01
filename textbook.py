

def convert_camel_to_snake(text):
    j = 0
    res = ""
    for char in text:
        if char.isupper():
            if j == 0:
                res += char.lower()
            else:
                res += "_" + char.lower()
        else:
            res += char
        j += 1
    return res  

s = "HelloWorld"

res = convert_camel_to_snake(s)
print(res)
