# append function in array

# creating an array

import array as ar

l = [1, 2, 4, 3, 5, 6, 8]

xy = ar.array("i", l)

print("Before appending the list is ")

for i in xy:
    # printing the elements

    print(i, end=" ")

xy.append(9)

print("Before appending the list is ")

print(xy)


# fromlist()

# this function is used to append the list at the end of the array

li = [99, 98, 100]

# using fromlist() function

xy.fromlist(li)


for i in xy:
    # printing the elements

    print(i, end=" ")


# to list() function

# used to transform a array in a list

x1 = xy.tolist()

print("The new list is ")

print(xy)
