
# * * * * *
# * * * *
# * * *
# * *
# *
  

def print_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()

# # Change the value of 'rows' to adjust the size of the pattern
rows = 5

print_pattern(rows)

