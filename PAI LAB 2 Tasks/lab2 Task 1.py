password = input("Enter your password: ")
if len(password) < 8:
   print("Incorrect Password")

for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char in "@#$%^&*()":
            has_special = True
if has_letter and has_digit and has_special:
        print("Password is Correct")
else:
        print("Incorrect Password")