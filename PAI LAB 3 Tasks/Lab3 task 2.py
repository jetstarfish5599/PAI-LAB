def is_vowel(user_input):
    vowels = 'aeiouAEIOU'
    if not user_input:
        return False
    last_letter = user_input[-1]
    return last_letter in vowels

string = input("Enter a string: ")
if is_vowel(string):
    print("The last letter is a vowel.")
else:
    print("The last letter is  a consonent.")
