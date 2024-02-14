fruit_list = ['apple', 'banana', 'cherry']
fruit_list.append('orange')
fruit_list.insert(1, "kiwi")
fruit_list.sort(key=len)
fruit_list.pop()
fruit_list.remove("kiwi")
fruit_list.index("apple")

print(fruit_list[-1])
print(f"fruit_list: {fruit_list}")

