password = input("Please enter a password: ")

is_long_enough = len(password) >= 8 
contains_letter = any(char.isalpha() for char in password)  
contains_number = any(char.isdigit() for char in password)  

if is_long_enough and contains_letter and contains_number:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")
