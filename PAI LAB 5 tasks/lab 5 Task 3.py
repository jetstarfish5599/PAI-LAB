try:
    # lists 
    list1 = input("Enter first list elements separated by spaces: ").split()
    list2 = input("Enter second list elements separated by spaces: ").split()

    #Check
    if len(list1) != len(list2):
        print("Error: Both lists must have the same number of elements.")
    else:
        my_dict = {}

        #Create dictionary
        for i in range(len(list1)):
            my_dict[list1[i]] = list2[i]

        #string form
        dict_string = ""
        for key in my_dict:
            dict_string += key + " : " + my_dict[key] + "\n"

        #Save to task3.txt
        with open("task3.txt", "w") as f:
            f.write(dict_string)

        print("Dictionary created and stored in task3.txt successfully.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: You don't have permission to write to the file.")
except Exception as e:
    print("An unexpected error occurred:", e)
