def fix_replacement_file(filename="replacement_needed.txt", wrong='z', right='o'):
    try:
        with open(filename, "r") as f:
            text = f.read()

        #for no error
        if wrong not in text:
            print(f"No '{wrong}' found in {filename}. No change needed.")
            print("Content:", text)
            return

        #replacement
        corrected = "".join([right if ch == wrong else ch for ch in text])

        with open(filename, "w") as f:
            f.write(corrected)

        print(f"Replaced all '{wrong}' with '{right}' in {filename}.")
        print("Corrected content:")
        print(corrected)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except PermissionError:
        print(f"Error: Permission denied to access {filename}.")
    except Exception as e:
        print("An unexpected error occurred:", e)


#function call
fix_replacement_file()
