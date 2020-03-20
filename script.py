from mygroup import groupmates as gm

limit = float(input('Введите средний балл\n'))

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        marks = student['marks']
        srball = 0
        for mark in marks:
            srball+=int(mark)
        srball /= len(marks)

        if srball < limit:
            continue
        print(student["name"].ljust(15),
        student["surname"].ljust(10), str(student["exams"]).ljust(30),str(student["marks"]).ljust(20))
        
print_students(gm)
