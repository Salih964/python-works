arr = [1, 2, 3, 4, 2, 5, 1]

def find_duplicates(arr):
  
  seen = set()
  duplicates = set()
  for num in arr:
    if num in seen:
      duplicates.add(num)
    else:
      seen.add(num)
  if duplicates:
    print("Duplicate elements:", ", ".join(map(str, duplicates)))
  else:
    print("No duplicate elements found")

find_duplicates(arr) 

