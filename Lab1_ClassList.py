"""
Write a program that asks for the names of all the classes you are taking
this semester.
Save these class names in a list.
Print all the items in the list, one per line.
"""

#class_list = []

# # ask for class name input
# class_name_str = input("What classes you are taking? ")
#
# # function that adds an item to the end of a list
# class_list.append(class_name_str)
# print(class_list)
#
# # for loop to ask for name of each class
# class_list = class_name_str.split()
# print("Class List:")
# for lists in range(len(class_list)):
#     print(lists)

# get input for number of classes to determine loop
class_number = int(input("How many classes are you taking? "))
# create a list of objects by appending class instances to the list
class_list = []

# function returns a sequence of numbers, in a given range
for c in range(0, class_number):
    class_name = input(f'What is your class {c + 1}? ')
    # appends an element to the end of the list
    class_list.append(class_name)

print("Here's a list of your classes: ")
# allows you to iterate across a given iterable/sequence to access each...
# ...item of the sequence with the help of its index
for c in range(len(class_list)):
    print(class_list[c])