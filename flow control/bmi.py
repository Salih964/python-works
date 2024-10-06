#bmi

weight_in_kg=int(input("enter weight"))

height_in_cm=int(input("enter height"))

height_in_meter=height_in_cm/100

#bmi= weight_in_kg/(height_in_meter)**2

bmi=weight_in_kg//(height_in_meter)**2

print(bmi)

#  <18  under weight 
if   bmi<18:
        print("Underweight")

# 18-25 healthy
elif  bmi<25:    
        print("Healthy weight")

# 25-30 over weight
elif  bmi<30:
        print("Overweight")

# 30-35 obese
elif  bmi<35:
        print("Obese")

# above 35 severe obesity
elif bmi>=35:
        print("Severe obesity")

