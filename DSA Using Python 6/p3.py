# reversing the elements of the array

# importing the array

import array as ar

# creating a list

l = [3, 4, 2, 1, 6, 7, 8]

# creating an array with list

a = ar.array("i", l)

print("The original array is ")

# iterating the array

for i in a:
    # printing the elements

    print(i, end=" ")

# reversing the elements of the array

a.reverse()

print("After reversing the array is ")

print(a)

# finding if an element is present in the array or not

if 4 in a:
    print("Yes the element is present ")

else:
    print("No the element is not present")
