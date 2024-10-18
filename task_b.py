grade_input = input("Please enter your grade (0 - 100): ")
if not grade_input.isdigit():
    print("Error: Please enter a number")
else:
    grade = int(grade_input)
    if grade < 0 or grade > 100:
        print("Error:Grades must be between 0 abd 100")
    else:
        if 80 <= grade <= 100:
            letter_grade = 'A'
        elif 60 <= grade <= 79:
            letter_grade = 'B'
        elif 50 <= grade <= 59:
            letter_grade = 'C'
        elif 40 <= grade <= 49:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        
        print(f"Your grade is:{letter_grade}")
