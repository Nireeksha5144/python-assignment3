n=int(input("Entr a number:"))
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

print(f"factorial of {n} is:",factorial(n))