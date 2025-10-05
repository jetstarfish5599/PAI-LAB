try:
    f = open("txt.txt", "r")

    text = f.read()
    f.close()

    char_count = len(text)
    word_count = len(text.split())

    print("Number of characters:", char_count)
    print("Number of words:", word_count)

except FileNotFoundError:
    print("Error: txt.txt not found.")
except PermissionError:
    print("Error: You don't have permission to read txt.txt.")
except Exception as e:
    print("An unexpected error occurred:", e)
