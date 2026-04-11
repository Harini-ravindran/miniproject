student={}
def add_student(name,marks):
    student[name]=marks
    print("student added")
def display_students():
    for name,marks in student.items():
        print(name,":",marks)
add_student("Harini",87)
add_student("Anita",90)
display_students()