# Employee salary calculator

employee_name = input("Enter Employee Name: ")
basic_sal = float(input("Enter Basic Salary:"))

hra_percentage = float(input("Enter HRA percentage: "))
da_percentage = float(input("Enter DA percentage: "))

hra = (basic_sal * hra_percentage)/100
da = (basic_sal * da_percentage)/100

other_allowances = float(input("Enter Other Allowances: "))
Professional_tax = float(input("Enter Professional Tax: "))

gross_sal = basic_sal + hra + da + other_allowances
net_sal = gross_sal - Professional_tax


print("\n\n--------------- Salary Slip ---------------")
print("Employee Name: ",employee_name)
print("\nBasic Salary: ₹",float(basic_sal))
print("HRA : ₹",float(hra))
print("DA  : ₹",float(da))
print("Allowances: ₹",float(other_allowances))
print("\nGross Salary: ₹",float(gross_sal))
print("\nProfessional Tax: ₹",float(Professional_tax))
print("\nNet Salary: ₹",float(net_sal))
print("\n-------------------------------------------")

