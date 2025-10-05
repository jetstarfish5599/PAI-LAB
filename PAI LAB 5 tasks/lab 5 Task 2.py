try:
    filename = "txt.txt"
    search_word = "file"
    replace_word = input("Enter word to replace 'file' with: ")

    with open(filename, "r") as f:
        text = f.read()

    new_text = text.replace(search_word, replace_word)

    with open(filename, "w") as f:
        f.write(new_text)

    print("All occurrences of 'file' have been replaced with", replace_word)

except FileNotFoundError:
    print("Error: txt.txt not found.")
except PermissionError:
    print("Error: You don't have permission to modify txt.txt.")
except Exception as e:
    print("An unexpected error occurred:", e)
