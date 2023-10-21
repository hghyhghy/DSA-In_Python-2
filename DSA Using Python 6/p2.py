# counting the occurance elements in the array

# creating an array

import array as ar

l = [2, 3, 4, 5, 6, 7, 5]

# creating an array

a1 = ar.array("i", l)

# iterating   through the  array

print("The original array  is ")

# using a for loop

for i in a1:
    # printing the elements

    print(i, end=" ")

# counting the occurance of 5

# by using count method

count = a1.count(5)

print(f"The occurance of 5 in the  {a1} is", count, "Times")
