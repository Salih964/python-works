
base_path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\fileopertions\\"


leap_year_path=base_path+"leap_year.txt"
century_year_Path=base_path+"century_year.txt"
years_path=base_path+"years.txt"


year_ref=open(years_path,"r")

century_ref=open(century_year_Path,"w")

leap_ref=open(leap_year_path,"w")

for line in year_ref:
    year=int(line.strip("\n"))

    if year%100==0:
      century_ref.write(str(year)+"\n")  

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
       leap_ref.write(str(year)+"\n") 
