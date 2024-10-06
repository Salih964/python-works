from json import load

f=open("C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\restcountries\\data.json","r",encoding="UTF-8")

data=load(f)
print(len(data))

# all country name
country_names=[p.get("name") for p in data]
print(country_names)

# all capital
all_capital=[p.get("capital") for p in data]
print(set(all_capital))

# countries in asia
country_location=[p.get("name") for p in data if p.get("region")=="Asia"]
print(country_location)

# countries which have population under 400000
population_filter=[p.get("name") for p in data if p.get("population")<=400000]
print(population_filter)

# q2 country with highest population
population=max(data,key=lambda dictionary:dictionary.get("population"))
print(population.get("name"))

# country boarders
country_boarders=[c.get("borders") for c in data if c.get("name")=="India"]
print(country_boarders[0])

# borders
boarders_filter=[c.get("name") for c in data if "borders" in c and "IND" in c.get ("borders")]
print(boarders_filter)

# country name with language_name

values={}

for c in data:
     lang_list=[]
     if "languages" in c:
        for l in c.get("languages"):
            
            lang_list.append(l.get("name"))
        values[c.get("name")]=lang_list
print(values.get("Afghanistan"))

# countries with indian rupee
for c in data:
    if "currencies" in c:
        for cur in c.get("currencies"):
            if cur .get("name")=="Indian rupee":
               print(c.get("name"))

# country with maximum area               
# largest_country=max(data,key=lambda c:int(c.get("Area")))
# print(largest_country.get("name"))
 
#  all countries with multiple time zone
timezone_filter=[c.get("name") for c in data if len (c.get("timezones"))>1]   
print(timezone_filter)      

# countriees starts with A
name_filter=[c.get("name") for c in data if c.get("name").startswith("I")]
print(name_filter)

# independent countries
independent=[c.get("name") for c in data if c.get("independent")==True]
print(independent)

# timezone
india_timezone=[c.get("timezones") for c in data if c.get("name")=="India"]
print(india_timezone[0][0])

afg_timezone=[c.get("timezones") for c in data if c.get("name")=="Afghanistan"]
print(afg_timezone[0][0])

# country utc 
time_zone_india=(india_timezone[0][0])
time_zone_afg=(afg_timezone[0][0])

india_offset=time_zone_india.lstrip("UTC").replace(":",".")
afg_offset=time_zone_afg.lstrip("UTC").replace(":",".")

print(india_offset)
print(afg_offset)

# offset
from datetime import datetime,timedelta

offset_india=timedelta(hours=float(india_offset))

offset_usa=timedelta(hours=float(afg_offset))

time_country1=datetime.utcnow()+offset_india
print("first",time_country1)

time_country2=datetime.utcnow()+offset_usa
print("second",time_country1)

time_diff=time_country1-time_country2
# print("time difference",time_diff.total_seconds()) #< 0 behind, > 0 ahead 

if(time_diff.total_seconds()>0):
    print("ahead")
else:
    print("behind")    