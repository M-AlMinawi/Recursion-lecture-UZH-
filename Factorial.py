# When using a small number of functions from a library, import those functions instead of the full library
from time import time
from numpy import mean
from sys import setrecursionlimit
import matplotlib.pyplot as plt

# Change maximum recursion depth
setrecursionlimit(5000)


# Define simple factorial function
def factorial(n):
    # Base case of 0! = 1
    if n == 0:
        return 1
    # Recursive case of n! = n * (n-1)!
    else:
        return n * factorial(n - 1)


factorial_terms = [1]  # List to store calculated factorial results, base case 0!=1 already included


# Define factorial that stores values in the list and reuses them
def factorial_memoization(n):
    # Case where the result has already been computed
    if len(factorial_terms) > n:
        return factorial_terms[n]
    else:
        factorial_terms.append(n * factorial_memoization(n - 1))
        return factorial_terms[-1]


# Define factorial using iteration (loop) instead of recursion
# While loop
def factorial_while(n):
    iter_param = 0
    ans = 1
    while iter_param < n:
        ans = ans * (iter_param + 1)
        iter_param += 1
    return ans


# For loop
def factorial_for(n):
    ans = 1
    li = range(1, n + 1)
    for num in li:
        ans = ans * num
    return ans


# Measure run-time of methods for 1000!,2000!,3000!,4000!
test_vals = [1000, 1500, 2000, 2500, 3000, 3500, 4000]
# Record average run-times for each of the values
runtime_normal = []
runtime_memo = []
runtime_while = []
runtime_for = []
# Test one value at a time
for val in test_vals:
    # Record individual runtimes for each iteration
    time_normal = []
    time_memo = []
    time_while = []
    time_for = []
    # Test 30 times to reduce variance between results
    for i in range(30):
        # Base method
        start = time()
        factorial(val)
        stop = time()
        time_normal.append(stop - start)

        # Memoization method
        start = time()
        factorial_memoization(val)
        stop = time()
        time_memo.append(stop - start)

        # While loop method
        start = time()
        factorial_while(val)
        stop = time()
        time_while.append(stop - start)

        # For loop method
        start = time()
        factorial_for(val)
        stop = time()
        time_for.append(stop - start)
    runtime_normal.append(mean(time_normal))
    runtime_memo.append(mean(time_memo))
    runtime_while.append(mean(time_while))
    runtime_for.append(mean(time_for))

# Plot runtime to showcase the difference between the methods
plt.figure(figsize=(13, 8), dpi=100)
plt.plot(test_vals, runtime_normal, marker="x", label='Recursive method')
plt.plot(test_vals, runtime_memo, marker="o", label='Memoization method')
plt.plot(test_vals, runtime_while, marker="^", label='While loop method')
plt.plot(test_vals, runtime_for, marker="v", label='For loop method')
plt.legend(loc='best')  # Adds legend in flexible spot
plt.title("Run-time of factorial function")  # Title of the graph
plt.xlabel("n")  # x-axis label
plt.ylabel("Run-time / s")  # y-axis label
plt.grid(which="major")  # adds major gridlines
plt.grid(which="minor")  # adds minor gridlines
plt.minorticks_on()  # adds minor ticks on the axes
plt.show()
