num = input("Enter a 4-digit number: ")

# swap 1 and 4 vs 2 and 3
swapped = num[3] + num[2] + num[1] + num[0]

# add 7 to each digit mod 10
encrypted = ""
for d in swapped:
    encrypted += str((int(d) + 7) % 10)

print("Encrypted number:", encrypted)
