# checking the type of the array

# importing the array

import array as ar

# creating a list

l = [3, 2, 4, 5, 90]

# creating an array from thet list

a = ar.array("i", l)

print("The  original array is ")

# using a for loop

for i in a:
    # printing the elements

    print(i, end=" ")

    print()

# printing the type of the array

print(a.typecode)


#  itemsize()  function

# this returns the size in bytes of a single array element

print(f"The itemsize of the {a} is ", a.itemsize, "Bytes")
