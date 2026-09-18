students = [
    {"name": "Ali", "marks": [80, 75, 90]},
    {"name": "Sara", "marks": [95, 88, 92]},
    {"name": "Hamza", "marks": [60, 70, 65]},
    {"name": "Ayesha", "marks": [85, 90, 80]}
]


def calculate_average(marks):
    if len(marks) == 0:
        return 0.00
    
    return sum(marks)/len(marks)


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def analyze_students(students):
    if len(students) == 0:
        return 
    for student in students:
        average = calculate_average(student["marks"])
        student["average"] = average
# here was a bugg, it was if average>90, then assign value to student ["grade"].. but we want grade regardless average is above 90 or less than 90
        student["grade"] = get_grade(average)
    return students


def highest_student(students):
    if len(students) == 0:
        return 
    highest = 0.00
    highest_student_name = ""
# here , there was a bug, the program was using > operator between student["average"](which is float).. and highest, (which is string).. we cant compare a string with float, so i update this part of code.
    for student in students:
        if student["average"] > highest:
            highest = student["average"]
            highest_student_name = student["name"]
    return highest_student_name

def lowest_student(students):
    if len(students) == 0:
        return 
    lowest = students[0]["average"]
    lowest_student_name = students[0]["name"]
    for student in students:
        if student["average"] < lowest:
            lowest = student["average"]
            lowest_student_name = student["name"]
    return lowest_student_name


def class_average(students):
    total = 0
    if len(students) == 0:
        return 

    for student in students:
        total += student["average"]

    return total / len(students)


def display_report(students):
    for student in students:
        print(
            f'{student["name"]} | '
            f'Average: {student["average"]:.2f} | '
            f'Grade: {student["grade"]}'
        )

    print()
    print("Highest Student:", highest_student(students))
    print("Lowest Student:", lowest_student(students))
    # added :.2f after calling class average
    print(f'Class Average: {class_average(students):.2f}')


analyze_students(students)
display_report(students)