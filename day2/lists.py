# Task 1: List (warm up)


rappers = ['carti', 'drake', 'ye', 'pbm', 'boat']

# # Getting artist from list
print(rappers[0])
print(rappers[-1])


# #  Task 2: Modifying and Slicing 


# # Modifying ye to Kanye
rappers[2] = 'kanye'
print(rappers)

# # Printing the middle 3 rappers
print(rappers[1:4])


# Task 3: List Edits


# Inserting Rapper
rappers.insert(1, 'kendrick')
print(rappers)

# Adding Rapper to the end of list
rappers.append('j.cole')
print(rappers)

# Removing Artist
rappers.remove('carti')
print(rappers)

# pop() removes and returns an item
popped = rappers.pop()  # same as pop(-1)

# 2) Print the list and the popped value
print(f"List now: {rappers}")
print(f"Popped: {popped}")


# Task 4: Loops


# enumerate gives (index, value); i gets the index (starting at 1), name gets the item
for i, name in enumerate(rappers, start=1):
	print(f"{i}. {name}")


# Task 5: Tuples (immutability)
# Tuples are immutable; commas make the tuple


# Declare variable with two floats
coords = (44.0, -124.0)

# Unpack coords into two variables (a, b)
a, b = coords
print(a, b)

# Changing value raises TypeError
# coords[0] = 0.0



