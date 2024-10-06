def count_vowels(input_string):
  """
  Counts the number of vowels in a given string.

  Args:
      input_string: The string to count vowels in.

  Returns:
      An integer representing the number of vowels in the string.
  """

  vowels = "aeiouAEIOU"  # Define all vowels (upper and lower case)
  vowel_count = 0
  for char in input_string:
    if char in vowels:
      vowel_count += 1  # Increment count if character is a vowel
  return vowel_count

# Example usage
test_string = "This is a string with 5 vowels!"
vowel_count = count_vowels(test_string)
print(f"String: '{test_string}'")
print(f"Number of vowels: {vowel_count}")
