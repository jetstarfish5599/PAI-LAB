list1 = input("Enter first list elements: ").split()
list2 = input("Enter second list elements: ").split()

# Check  same length
if len(list1) != len(list2):
    print("Error: Both lists must have the same number of elements.")
else:
    #using zip
    my_dict = dict(zip(list1, list2))
    print("The resulting dictionary is:", my_dict)
