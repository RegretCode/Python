# Calculate the compound interest for a given principal amount, interest rate, and time period.
# FV = P*(1+R/N)^(N*T)
# FV is the future value of the loan or investment, P is the initial principal amount, R is the annual interest rate, N represents the number of times interest is compounded per year, and T represents time in years.

p = float(input("Insert the intital parincipal amount: "))
r = float(input("\nInsert the anaual interest rate: "))
n = float(input("\nInsert the number of times interest is compounded per year: "))
t = float(input("\nInsert the represented time in years: "))

fv = (p * ((1 + r/100) ** t) - p)

print(fv)
