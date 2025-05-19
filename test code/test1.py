student_count = int(input('enter student count: '))

for i in range(1, student_count + 1):
    student_score = int(input('enter student score: '))
    if student_score >= 50:
        print('D')
    elif student_score >= 55:
        print('D+')
    elif student_score >= 60:
        print('C')
    elif student_score >= 65:
        print('C+')
    elif student_score >= 70:
        print('B')
    elif student_score >= 75:
        print('B+')
    elif student_score >= 80:
        print('A')
    else:
        print('F')