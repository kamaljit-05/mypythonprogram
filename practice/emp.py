'''you want a Python program (WAP) that uses loops, functions, and classes to calculate an employee’s salary based on their working hours. Let me show you a clean example:'''
class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
    
    def log_hours(self, hours):
        self.hours_worked += hours
    
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


def main():
    employees = []
    n = int(input("Enter number of employees: "))
    
    # Loop to create employee objects
    for i in range(n):
        name = input(f"Enter name of employee {i+1}: ")
        rate = float(input(f"Enter hourly rate for {name}: "))
        emp = Employee(name, rate)
        
        # Loop to log working hours
        days = int(input(f"Enter number of working days for {name}: "))
        for d in range(days):
            hrs = float(input(f"Enter hours worked on day {d+1}: "))
            emp.log_hours(hrs)
        
        employees.append(emp)
    
    # Display salaries
    print("\n--- Salary Slips ---")
    for emp in employees:
        print(f"{emp.name}: ₹{emp.calculate_salary():.2f}")


# Run the program
if __name__ == "__main__":
    main()

    