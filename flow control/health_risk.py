tummy_size=int(input("enter tummy size"))
buttock_size=int(input("enter buttock size"))
gender=input("enter gender")

value=tummy_size/buttock_size

value=round(value,2)

if gender=="male":
 
#  0.95 or below low 
 if value<=.95:
    print("low health risk")
# 0.96 to 1.0 moderate
elif value<=1.0:
    print("moderate health risk")
# 1.0>above
elif value>1:
    print("high health risk")

elif gender=="female":
 
#  <.80 or below low health
 if value<=.80:
    print("low health risk")
#  0.81 - 0.85 moderate health
elif value<=.85:
   print("moderate health risk")
# 0.85> high health risk
elif value >.85:
    print("high health risk")
