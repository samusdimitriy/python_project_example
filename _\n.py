def real_len(text):
    sum = 0
    symbols = ['\n', '\f', '\r', '\t', '\v']
    for char in text:
        if char not in symbols:
            sum += 1
    return sum