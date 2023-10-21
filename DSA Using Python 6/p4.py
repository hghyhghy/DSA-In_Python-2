# extending the   elements of the array

# importing the array

import array as ar

# creating a list

l1 = [2, 1, 4, 3, 6, 5, 8, 7]

a = ar.array("i", l1)

print("The original array is ")

# iterating through the array

# using for loop

for i in a:
    # printing the elements

    print(i, end=" ")

#  extending some values with that array

a.extend([99, 98, 87, 76])

print("After extending the array becomes ")

print(a)
