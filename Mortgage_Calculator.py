#Ask the user for principal, yearly interest and years
principal=float(input('What is your principal? \n'))
yearlyInterest=float(input('What is your yearly interest? \n'))
years=int(input('For how many years? \n'))
print()

# prepare variables for formulas
p=principal
i=(yearlyInterest/100)/12
n=years*12

#create formulas
mortgage=p*(i*(1+i)**n)/((1+i)**n-1)
totalAmount=mortgage*n

#Print results
print(f'For a {years}-year mortgage of ${principal:.2f} at an annual interest rate of {yearlyInterest}% you pay ${mortgage:.2f} monthly')
print(f'Total amount paid will be ${totalAmount:.2f}\n')