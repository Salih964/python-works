
# all years(1)
years=[]
century_years=[]
non_century_years=[]
leap_years=[]

for y in range(1800,2025):
    years.append(y)
# print("all years",years) 

# century year and non century (2)
for y in years:
    if y%100==0:
        century_years.append(y)
    else:
        non_century_years.append(y)

# print("century years",century_years)
# print("non century years",non_century_years) 
        
# leap year(3)
for y in years:
    if(y%100==0 and y%400==0) or(y%100!=0 and y%4==0):
        leap_years.append(y)

print("leap years",leap_years) 
print("number of leap years from 1800-2024",len(leap_years))

