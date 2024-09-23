# Get user input for salary and loan amount
salary = int(input("Enter your monthly salary: "))
loanAmount = float(input("Enter the amount you want to loan: "))

    # Check eligibility
if salary >= 30000:
    if loanAmount <= (salary * 10):
            # Eligible for loan
            months = int(input("How many months will you pay the loan? "))
            #10% interest
            interest = loanAmount * 0.10  
            totalAmount = loanAmount + interest
            monthly_payment = totalAmount / months

            print(f"Congrats! Your request for loan has been approved!")
            print(f"Total Amount you need to pay (including interest): {totalAmount:.2f}")
            print(f"Monthly Payment: {monthly_payment:.2f}")
    else:
            print("Not approved: The loan amount requested exceeds 10 times your monthly salary.")
else:
    print("Not approved: Your poor and your monthly salary is less than 30,000.00.")