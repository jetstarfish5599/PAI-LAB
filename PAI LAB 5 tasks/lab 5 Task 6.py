def save_question():
    try:
        sentence = input("Enter a sentence: ")

        if sentence.strip().endswith("?"):
            with open("questions.txt", "w") as f:
                f.write(sentence)
            print("Question saved in questions.txt.")
        else:
            print("This is not a question.")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print("An unexpected error occurred:", e)

save_question()
