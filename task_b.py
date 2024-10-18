grade_input = input("Please enter your grade (0 - 100): ")
try:
    grade = float(grade_input)  # Use float to allow decimal grades
except ValueError:
    print("Error: Please enter a number")
    exit()  

if grade < 0 or grade > 100:
    print("Error: Grades must be between 0 and 100")
    exit() 

if 80 <= grade <= 100:
    letter_grade = 'A'
elif 60 <= grade < 80:
    letter_grade = 'B'
elif 50 <= grade < 60:
    letter_grade = 'C'
elif 40 <= grade < 50:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f"Your grade is: {letter_grade}")
