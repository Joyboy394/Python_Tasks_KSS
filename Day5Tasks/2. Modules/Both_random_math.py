import random
import math

numbers = [random.randint(1, 200) for _ in range(20)]
print(f"Random numbers: {numbers}")

maximum = max(numbers)
minimum = min(numbers)
sqrt_max = math.sqrt(maximum)
log_min = math.log(minimum)

print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")
print(f"Square root of maximum ({maximum}): {sqrt_max:.4f}")
print(f"Logarithm of minimum ({minimum}): {log_min:.4f}")
