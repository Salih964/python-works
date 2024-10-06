string = "A2B4C6"
def sort_string_symbols_digits(string):
  
  symbols = []
  digits = []
  for char in string:
    if char.isalpha():
      symbols.append(char)
    elif char.isdigit():
      digits.append(char)
  return "".join(symbols) + "".join(digits)


sorted_string = sort_string_symbols_digits(string)
print("Sorted string:", sorted_string)
