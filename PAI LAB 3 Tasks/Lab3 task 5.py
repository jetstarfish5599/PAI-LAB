def is_palindrome(word):
    word = word.lower()

    if word == word[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

is_palindrome("madam")

