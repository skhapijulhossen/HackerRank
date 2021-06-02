def gradingStudents(grades):
    # Write your code here
    filtered_grades = []
    for grade in grades:
        up = ((grade // 5) + 1) * 5
        if (up - grade) < 3 and grade >= 38:
            filtered_grades.append(up)
        else:
            filtered_grades.append(grade)
    return filtered_grades