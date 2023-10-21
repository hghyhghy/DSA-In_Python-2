# indexing an array

# to search the first occurance index of the array

# creating an array

import array as ar


l = [2, 1, 4, 3, 6, 5, 8, 7]


# creating an array

a = ar.array("i", l)

print("The original array is ")

# using a for loop

for i in a:
    # printing the elements of the array

    print(i, end=" ")


# printing the index

print(f"The index of the first occurance 1 in the array {a} is ")

print(a.index(1))


print(f"The index of the first occurance 8 in the array {a} is ")

print(a.index(8))
