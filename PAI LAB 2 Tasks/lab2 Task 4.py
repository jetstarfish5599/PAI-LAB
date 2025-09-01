numbers = (5, 10,15, 20, 25,30)
a = min(numbers)
numbers_list = list(numbers)
#removing smallest number to similarly get second smallest 
numbers_list.remove(a)
#for second smallest same method as first smallest was removed
b = min(numbers_list)
print(a, b)