# Day 13: Student Marks Analyzer

# Students and their marks
students = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [85, 92, 78, 88, 95]

total = 0
for i in range(5):
    score = marks[i]

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{students[i]}: {score} – Grade {grade}")
    total += score

# Average
average = total / 5
print(f"Average marks: {average:.1f}")
