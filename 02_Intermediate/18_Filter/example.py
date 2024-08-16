

grades = [91, 83, 58, 75, 67, 45, 89]

def is_passing(grade):
    return grade >= 60

passing_grades = filter(is_passing, grades)

passing_grades_list = list(passing_grades)
print(passing_grades_list)

# ------------

passing_grades = filter(lambda grade: grade >= 60, grades)
passing_grades_list = list(passing_grades)
print(passing_grades_list)
