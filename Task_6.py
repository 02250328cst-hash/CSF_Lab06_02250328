import time
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
call_count = 0
def fibonacci_recursive(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
n = int(input("Enter number: "))
start = time.time()
iter_result = fibonacci_iterative(n)
iter_time = time.time() - start
call_count = 0
start = time.time()
rec_result = fibonacci_recursive(n)
rec_time = time.time() - start
print("Iterative Fibonacci =", iter_result)
print("Recursive Fibonacci =", rec_result)
print("Recursive Calls =", call_count)

if iter_time < rec_time:
    print("Iterative is more efficient")
else:
    print("Recursive is more efficient")