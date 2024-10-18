day_input = input("please enter a day of the week: ")
day = day_input.strip().capitalize()
days_of_week = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}
if day in days_of_week:
    print(f"{day} is day {days_of_week[day]}")
else:
    print("Please enter a valid day")