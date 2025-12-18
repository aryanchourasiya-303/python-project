class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        self.status = "Working"

    def _str_(self):
        return (
            f"Employee Name : {self.name}\n"
            f"Age           : {self.age}\n"
            f"Department    : {self.department}\n"
            f"Status        : {self.status}\n"
        )


class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = {}
        print(f"\n🏢 Welcome to {self.company_name}")
        print("Employee System Started Successfully\n")

    def add_employee(self, emp_id, employee):
        try:
            if not isinstance(employee, Employee):
                raise TypeError
            self.employees[emp_id] = employee
            print("Employee added successfully\n")
        except TypeError:
            print("Invalid employee data\n")

    def remove_employee(self, emp_id):
        try:
            self.employees[emp_id].status = "Left Company"
            print("Employee removed successfully\n")
        except KeyError:
            print("Employee ID not found\n")

    def update_department(self, emp_id, new_department):
        try:
            self.employees[emp_id].department = new_department
            print("Department updated successfully\n")
        except KeyError:
            print("Employee ID not found\n")

    def view_employees(self):
        print("\n------- Employee Records -------")
        if not self.employees:
            print("No employees found\n")
        else:
            for eid, employee in self.employees.items():
                print(f"Employee ID : {eid}")
                print(employee)
        print("--------------------------------\n")

    def search_employee(self, emp_id):
        if emp_id in self.employees:
            print("\nEmployee Found:")
            print(self.employees[emp_id])
        else:
            print("Employee not found\n")

    def delete_employee(self, emp_id):
        try:
            del self.employees[emp_id]
            print("Employee record deleted\n")
        except KeyError:
            print("Employee ID not found\n")


# ---------------- MENU ----------------
company = Company("TechVision Pvt Ltd")

while True:
    print("----- MENU -----")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Department")
    print("4. View Employees")
    print("5. Search Employee")
    print("6. Delete Employee Record")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        try:
            age = int(input("Enter Age: "))
            dept = input("Enter Department: ")
            company.add_employee(eid, Employee(name, age, dept))
        except ValueError:
            print("Age must be a number\n")

    elif choice == "2":
        eid = input("Enter Employee ID: ")
        company.remove_employee(eid)

    elif choice == "3":
        eid = input("Enter Employee ID: ")
        dept = input("Enter New Department: ")
        company.update_department(eid, dept)

    elif choice == "4":
        company.view_employees()

    elif choice == "5":
        eid = input("Enter Employee ID: ")
        company.search_employee(eid)

    elif choice == "6":
        eid = input("Enter Employee ID: ")
        company.delete_employee(eid)

    elif choice == "7":
        print("Exiting Employee System... Goodbye!")
        break

    else:
        print("Invalid choice, try again\n")