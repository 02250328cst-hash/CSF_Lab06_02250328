def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)
num = int(input("Enter number: "))
print("Iterative factorial =", iterative_factorial(num))
print("Recursive factorial =", recursive_factorial(num))