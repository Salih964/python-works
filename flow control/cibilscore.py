cibil_score=int(input("enter your cibil score"))

# <550 poor
if cibil_score<550:
    print("poor")

# 550- 649 average
elif cibil_score<650:
    print("average")

# 650-750 good
elif cibil_score<750:
    print("good") 

#>750  excellent
elif cibil_score>=750:
    print("excellent")


