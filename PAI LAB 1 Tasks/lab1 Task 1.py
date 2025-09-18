num = int(input("Enter a number: "))
num_float = float(num)
num_str = str(num)
num_complex = complex(num)

print("Float:", num_float, " Type:", type(num_float))
print("String:", num_str, " Type:", type(num_str))
print("Complex:", num_complex, " Type:", type(num_complex))

if (num // 2) * 2 == num:
    print(num, "is divisible by 2")
else:
    print(num, "is not divisible by 2")
