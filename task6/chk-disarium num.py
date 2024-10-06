number=175

def is_disarium(n):
  
  sum_of_digits = 0
  digits = [int(d) for d in str(n)]
  for i, digit in enumerate(digits):
    sum_of_digits += digit ** (i + 1)
  return sum_of_digits == n

print(f"{number} is a Disarium number: {is_disarium(number)}")
