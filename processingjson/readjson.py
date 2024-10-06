from json import load

path="C:\\Users\\2\\OneDrive\\Desktop\\mypython works\\processingjson\\students.json"

f=open(path,"r")

data=load(f)

for dictionary in  data:
    print(dictionary.get("name"))
    print(dictionary.get("course"))

# print students from thrissur
    
# for dictionary in data:
#     if dictionary.get("place")=="thrissur":
#         print(dictionary.get("name")) 
            #or

place_filter=[dictionary.get("name") for dictionary in data if dictionary.get("place")=="thrissur"] 
print(place_filter)       

# print all courses

# course_filter=[dictionary.get("course")for dictionary in data if dictionary.get("course")]
# print(course_filter)

st=set()
for dictionary in data:
    course=dictionary.get("course")
    st.add(course)

print(st)  

#  #  #
dictionary1={"one":1,"two":2,"three":3}
dictionary2={"four":4,"five":5,"six":6}

newdictionary={**dictionary1,**dictionary2}
print(newdictionary)