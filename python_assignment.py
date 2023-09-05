class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        result = [emp for emp in self.employees if emp.age == age]
        return result

    def search_by_name(self, name):
        result = [emp for emp in self.employees if emp.name == name]
        return result

    def search_by_salary(self, operator, salary):
        operators = {'>': lambda x, y: x > y,
                     '<': lambda x, y: x < y,
                     '>=': lambda x, y: x >= y,
                     '<=': lambda x, y: x <= y}
        
        result = [emp for emp in self.employees if operators[operator](emp.salary, salary)]
        return result

def main():
    db = EmployeeDatabase()

    # Populate the employee database with sample data
    db.add_employee(Employee("161E90", "Raman", 41, 56000))
    db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("\nSearch options:")
        print("1. Search by Age")
        print("2. Search by Name")
        print("3. Search by Salary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            age = int(input("Enter age to search: "))
            result = db.search_by_age(age)
        elif choice == '2':
            name = input("Enter name to search: ")
            result = db.search_by_name(name)
        elif choice == '3':
            operator = input("Enter salary operator (>, <, <=, >=): ")
            salary = int(input("Enter salary to compare: "))
            result = db.search_by_salary(operator, salary)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            continue

        if not result:
            print("No matching records found.")
        else:
            print("\nMatching records:")
            for emp in result:
                print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    main()