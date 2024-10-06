number = 18
def is_harshad(n):
  
  return n % sum(int(d) for d in str(n)) == 0


print(f"{number} is a Harshad number: {is_harshad(number)}")
