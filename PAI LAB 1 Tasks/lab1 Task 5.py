name = "masoom"
year = "0001"

part1 = name[:3]
part1 = part1.capitalize()

part2 = year[-2:]

symbols = "@#%&*"
ascii_val = ord(name[0])
part3 = symbols[ascii_val % len(symbols)]

password = part1 + part2 + part3
print("Generated password:", password)
