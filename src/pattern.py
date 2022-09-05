
# Print the pattern

symbol_list = []

for i in range(9):
    if i < 5:
        symbol_list.append('*')
        print(" ".join(symbol_list))
        continue
    symbol_list.pop()
    print(" ".join(symbol_list))
