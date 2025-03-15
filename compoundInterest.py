p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (%): ")) / 100
t = float(input("Enter time in years: "))
n = int(input("Enter number of times interest is compounded per year: "))

ci = p * (1 + r/n) ** (n*t)
print("Compound Interest:", ci - p)
