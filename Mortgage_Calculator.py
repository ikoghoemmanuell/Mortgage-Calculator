# principal=1000000
# interest=7.5
# years=30

principal=int(input('type principal'))
interest=float(input('type interest'))
years=int(input('type number of years'))

p=principal
i=(interest/100)/12
n=years*12

mortgage=p*(i*(1+i)**n)/((1+i)**n-1)
totalAmount=mortgage*n

print(f'For a {years}-year mortgage of ${principal} at an annual interest rate of {interest}% you pay ${mortgage} monthly')
print()
print(f'Total amount paid will be ${totalAmount}')