students = [
    {"name": "Ali", "marks": [80, 75, 90]},
    {"name": "Sara", "marks": [95, 88, 92]},
    {"name": "Hamza", "marks": [60, 70, 65]},
    {"name": "Ayesha", "marks": [85, 90, 80]}
]


def calculate_average(marks):
    return sum(marks) / len(marks)


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
    for student in students:
        average = calculate_average(student["marks"])
        student["average"] = average

        if average > 90:
            student["grade"] = get_grade(average)

    return students


def highest_student(students):
    highest = 0

    for student in students:
        if student["average"] > highest:
            highest = student["name"]

    return highest


def class_average(students):
    total = 0

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
    print("Class Average:", class_average(students))


analyze_students(students)
display_report(students)