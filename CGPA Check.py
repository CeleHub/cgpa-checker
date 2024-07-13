# A Simple Python Code To Calculate GPA

def calculate_gpa(grades, credit_unit):
    total_grade_points = 0
    total_credits = 0
    
    # Ensure grades and credit_unit lists are of the same length
    if len(grades) != len(credit_unit):
        print("Error: The length of grades and credit unit lists should be the same.")
        return None
    
    # Calculate total grade points and total credits
    for i in range(len(grades)):
        total_grade_points += grades[i] * credit_unit[i]
        total_credits += credit_unit[i]
    
    # Calculate GPA
    gpa = total_grade_points / total_credits
    return gpa

# Collecting user input
num_courses = int(input("Enter the number of courses: "))
grades = []
credit_unit = []

for i in range(num_courses):
    letter = str(input(f"Enter the grade letter for course {i+1}: "))
    if letter == "A": grade = 5
    elif letter == "a": grade = 5
    elif letter == "B": grade = 4
    elif letter == "b": grade = 4
    elif letter == "C": grade = 3
    elif letter == "c": grade = 3
    elif letter == "D": grade = 2
    elif letter == "d": grade = 2
    elif letter == "F": grade = 0  
    elif letter == "f": grade = 0
    elif letter == "P": grade = 5 
    elif letter == "p": grade = 5
    else: print("Invalid Input!")
    
    credits = int(input(f"Enter the credit unit(s) for course {i+1}: "))
    grades.append(grade)
    credit_unit.append(credits)

# Calculate GPA
gpa = calculate_gpa(grades, credit_unit)
if gpa is not None:
    print(f"Your GPA is: {gpa:.2f}")

if gpa > 5.0:
    print("ERROR! GPA > 5.0!")
elif gpa >= 4.5:
    print("First Class 🫡")
elif gpa >= 3.5:
    print("Second Class Upper! ✊")   
elif gpa >= 2.5:
    print("Second Class Lower! 👏")
elif gpa >= 1.5:
    print("Third Class! 😮‍💨")
else:
    print("Advised To Withdraw! 🤝")

# TO FIND CGPA

cgparequest = str(input("Need to find CGPA? y/n: "))
if cgparequest == "Y":
    currentcgpa = float(input("Current GPA/CGPA: "))
    cgpa = str((currentcgpa + gpa) / 2)
    print("Your new CGPA is "+ cgpa+ " 😌")
elif cgparequest == "y":
    currentcgpa = float(input("Current GPA/CGPA: "))
    cgpa = str((currentcgpa + gpa) / 2)
    print ("Your new CGPA is "+ cgpa+ " 😌")
elif cgparequest == "N":
    print("Thanks 🙃")
elif cgparequest == "n":
    print("Thanks 🙃")
else: print("Invalid Input 🫨")