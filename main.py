import loanclient

loan_client = loanclient.LoanClient()

loan = loan_client.create_loan(10000, .0551, 36)

print("Below is the response from creating a loan")
print(loan)

loan_grabbed = loan_client.get_loan(loan['id'])

print("Below is the response from grabbing the loan we created")
print(loan_grabbed)

updated_loan = loan_client.update_loan(loan['id'], loan['amount'], loan['interest_rate'] + .01, loan['length'])

print("Below we have added 1% to the interest rate of the loan")
print(updated_loan)

second_loan_grabbed = loan_client.get_loan(loan['id'])

print("Below we have grabbed the loan one final time, to confirm that our updated changes worked")
print(second_loan_grabbed)


