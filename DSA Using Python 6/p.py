# array slicing

# importing array

import array as ar

# creating  a list first

l = [2, 1, 4, 3, 6, 5, 8, 7]


# making the list as an array


a = ar.array("i", l)

print("The initial array is ")

# using a for loop to iterate

for i in a:
    # printing the array

    print(i, end=" ")

print(f"The sliced array from the array {a} is ")

print(a[3:8])

# another slicing for 5 to rest

print(f"The sliced array from the array {a} is ")


print(a[5 : len(a)])
