# updating  the array elements

# creating an array

import array as ar

l = [2, 1, 4, 3, 6, 5, 8, 7]

a = ar.array("i", l)

print("The original array is ")

# using a for loop

for i in l:
    # printing the elements

    print(i, end=" ")


# updating the elements

print("The updated  array is ")

a[3] = 99

print(a)

# updating other elements

print("The updated  array is ")


a[4] = 100

print(a)
