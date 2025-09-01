students = {"ali": 748, "ahmed": 92, "anwar": 815, "zain": 60, "zahid": 90}
#Updatung students
students["anwar"]= 85
students["ali"] =78
#delete a student       
del students["zain"]          
topper = max(students, key=students.get)

print("Students:", students)
print("Topper:", topper, students[topper])