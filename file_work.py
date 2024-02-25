fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)  # 6
fh.close()
