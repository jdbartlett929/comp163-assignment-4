student_name = "Julian Bartlett"
current_gpa = 4.0
study_hours = 25
social_points = 50
stress_level = 40

print("Welcome to College Life,", student_name)
print("Starting stats -> GPA:", current_gpa, "Study:", study_hours, "Social:", social_points, "Stress:", stress_level)

print()
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")
choice = input("Your choice: ")

if choice == "A":
    if current_gpa >= 3.0:
        study_hours = study_hours + 5
        stress_level = stress_level - 5
    else:
        study_hours = study_hours + 3
        stress_level = stress_level - 2
elif choice == "B":
    if current_gpa >= 3.0:
        study_hours = study_hours + 8
        stress_level = stress_level + 5
    else:
        study_hours = study_hours + 10
        stress_level = stress_level + 10
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours = study_hours + 15
        stress_level = stress_level + 15
    else:
        study_hours = study_hours + 18
        stress_level = stress_level + 25
else:
    print("Invalid choice")

options = ["Programming", "Math", "English", "History"]
print()
print("Pick a study focus from:", options)
focus = input("Your focus: ")

if focus in options:
    if (focus == "Programming" or focus == "Math") and study_hours >= 30:
        current_gpa = current_gpa + 0.1
        social_points = social_points - 5
    elif (focus == "English" or focus == "History") and social_points >= 60:
        current_gpa = current_gpa + 0.05
        social_points = social_points - 2
    elif not (stress_level <= 70):
        current_gpa = current_gpa - 0.1
        stress_level = stress_level + 5
    else:
        current_gpa = current_gpa + 0.02
else:
    print("Invalid focus")

if type(social_points) is not int:
    social_points = int(social_points)

if type(study_hours) is int and type(current_gpa) is float:
    if current_gpa >= 3.7:
        if stress_level <= 60 and social_points >= 40:
            ending = "Dean's List"
        else:
            ending = "High GPA, High Stress"
    elif current_gpa >= 3.0:
        if social_points >= 60 and stress_level < 70:
            ending = "Balanced Scholar"
        else:
            ending = "Average Semester"
    else:
        if social_points >= 70 or study_hours < 20:
            ending = "Too Social, Low GPA"
        else:
            ending = "Probation Risk"
else:
    ending = "Type Check Failed"

print()
print("=== Final Statistics ===")
print("GPA:", round(current_gpa, 2))
print("Study Hours:", study_hours)
print("Social Points:", social_points)
print("Stress Level:", stress_level)
print("Ending:", ending)
