# Get user input for salary and loan amount
salary = float(input("Enter your monthly salary: "))
loanAmount = float(input("Enter the amount you want to loan: "))

# Check eligibility
if salary >= 30000:
    if loanAmount <= (salary * 10):
            # Eligible for loan
            months = int(input("How many months do you plan to pay back the loan? "))
            interest = loanAmount * 0.10  # 10% interest
            totalAmount = loanAmount + interest
            monthly_payment = totalAmount / months

            print(f"Loan Approved!")
            print(f"Total Amount to be paid (including interest): {totalAmount:.2f}")
            print(f"Monthly Payment: {monthly_payment:.2f}")
    else:
            print("Not approved: The loan amount requested exceeds 10 times your monthly salary.")
else:
    print("Not approved: Your monthly salary is less than 30,000.00.")