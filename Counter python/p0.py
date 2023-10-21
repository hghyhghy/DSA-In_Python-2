# substarcting two xounters

from collections import Counter

# setting two counters

c1 = Counter(a=10, b=9, c=99)

c2 = Counter(a=1, b=7, c=90)

# substracting two counters

c1.subtract(c2)

print(c1)

# we can use counter to get distinct elements from a list

# creating a list

li = ["Subham", "Shreyoshi", "Shrestha", "Subham"]

print(Counter(li))


# printing all counter values

my_counter = Counter("abracsdge")

print(my_counter.keys())

print(my_counter.values())

print(my_counter.items())
