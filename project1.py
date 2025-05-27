# Project 1: A simple Earnings Calculator
# three prompts : employee's name, hourly wage, how many hours worked
# All employee names should be stripped of any excess white space, and should be in title case.
# Output: Regina George earned $800 this week.

employee_name = input("Name and surname of employee: ").strip().title()
hourly_rate = input("What is the employees hourly wage: $")
hours_worked = input("How many hours has the employee worked: ")

total_hours = float(hourly_rate) * float(hours_worked)

print(f"{employee_name} earned ${str(total_hours)} this week.")