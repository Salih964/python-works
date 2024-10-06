def find_sum_common_elements(arr1, arr2):
  """
  Finds the sum of common elements in two arrays.
  """
  common_elements = set(arr1) & set(arr2)  # Find common elements using sets
  return sum(common_elements)  # Calculate and return the sum

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1, 1]
print(find_sum_common_elements(arr1, arr2))  # Output: 15
