string = "my python"

def even_odd_characters(string):
     
  even_chars = ""
  odd_chars = ""
  for i, char in enumerate(string):
    if i % 2 == 0:
      even_chars += char
    else:
      odd_chars += char
  print("Even characters:", even_chars)
  print("Odd characters:", odd_chars)

even_odd_characters(string)
