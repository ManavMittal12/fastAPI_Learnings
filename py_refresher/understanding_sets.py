my_set = {1, 2, 3, 4, 5, 1, 5}

print(my_set)
print(len(my_set))


for i in my_set:
    print(i)
    

# Since, sets are unordered and can be anywhere in the memory location,
# we can't use indexing/subscripting.    
# print(my_set[1])    # TypeError: 'set' object is not subscriptable


# to remove an element in the set, we have to use 
# discard method 
my_set.discard(3)
print(my_set)

# we can use clear method and it will remove all elements from the set 
my_set.clear()
print(my_set)

# we can add an element back by using the add functionality.
my_set.add(6)
print(my_set)


# we can also add more than one element in a set using 
# update method.
# it takes an iterable as an argument.
my_set.update([7, 8])
print(my_set)
my_set.update((9, 10))
print(my_set)
