def element_exists(list_to_check, index):
 
  try:
    list_to_check[index]
    return True
  except IndexError:
    return False

# Example usage
my_list = [1, 2, 3, 4, 5]

print("Is element at index 2 present?", element_exists(my_list, 2))
print("Is element at index 10 present?", element_exists(my_list, 10))
