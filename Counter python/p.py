# python program to show different ways to create a  counter

# importing counter

from collections import Counter

# with sequence of items

print(Counter(["b", "a", "b", "c", "a", "c"]))

# with dictionary

print(Counter({"a": 2, "b": 2, "c": 2}))

# with keywords arguments

print(Counter(a=2, b=2, c=2))


# approcah 2

# by using update method

count = Counter()

count.update([1, 2, 1, 3, 4, 3, 5, 4, 6, 7])

print(count)

count.update([1, 2, 4])

print(count)
