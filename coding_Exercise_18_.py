student_marks = {
    'jenny':92,
    'harry':78,
    'dimpy':56,
    'rahul':41,
    'aniket':99,
    'prem':34,
    'aman':1000
}
for i in student_marks:
    if 91 <= student_marks[i] <= 100 :
        student_marks[i] = 'A+'
    elif 81 <= student_marks[i] <= 90 :
        student_marks[i] = 'A'
    elif 71 <= student_marks[i] <= 80 :
        student_marks[i] = 'B+'
    elif 61 <= student_marks[i] <= 70 :
        student_marks[i] = 'B'
    elif 51 <= student_marks[i] <= 60 :
        student_marks[i] = 'C'
    elif 41 <= student_marks[i] <= 50 :
        student_marks[i] = 'D'
    elif 40 > student_marks[i] :
        student_marks[i] = 'F'
else:
    print('Error')
print(student_marks)
#Expected type 'int' (matched generic type '_VT'), got 'str' instead
