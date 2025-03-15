def lcm(a, b):
    return (a * b) // math.gcd(a, b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("LCM is:", lcm(a, b))
