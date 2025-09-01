students = [("ali", 748), ("ahmed", 92), ("anwar", 815), ("zain", 60), ("zahid", 90)]

def get_marks(student):
    return student[1]

students.sort(key=get_marks, reverse=True)

for s in students[:3]:
    print(s[0], s[1])