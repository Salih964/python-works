def remove_duplicates(input_string):
  """
  Removes duplicate characters from a string while preserving order.

  Args:
      input_string: The string to remove duplicates from.

  Returns:
      A new string with duplicates removed.
  """

  seen = set()  # Use a set to efficiently track seen characters
  output_string = ""
  for char in input_string:
    if char not in seen:
      seen.add(char)  # Add unique characters to the set
      output_string += char  # Append unique characters to the output string
  return output_string

# Example usage:
test_string = "Mississippi!!"
result = remove_duplicates(test_string)
print(f"Original string: {test_string}")
print(f"String with duplicates removed: {result}")
