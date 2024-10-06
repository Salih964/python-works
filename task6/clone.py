original_list = [1, 2, 3, 4, 5]
cloned_list = original_list[:]

print(f"Original list: {original_list}")
print(f"Cloned list: {cloned_list}")

# example usage
original_list[2] = 99

print(f"Original list after modification: {original_list}")
print(f"Cloned list remains unchanged: {cloned_list}")
