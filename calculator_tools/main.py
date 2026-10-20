from .arithmetic import calculator
from .converter import temp_converter
from .exceptions import safe_divide
from .statistics import *

print(calculator("add", 10, 5))
print(calculator("subtract", 10, 5))
print(calculator("multiply", 10, 5))
print(calculator("divide", 10, 5))

try:
    print(calculator("divide", 10, 0))
except ValueError as e:
    print(f"Error: {e}")

print(temp_converter("celsius", 98.6))
print(temp_converter("fahrenheit", 37))

print(safe_divide(10, 5))
try:
    print(safe_divide(10, 0))
except ValueError as e:
    print(f"Error: {e}")

print(calculate_mean([1, 2, 3, 4, 5]))
print(calculate_median([1, 2, 3, 4, 5]))
print(calculate_mode([1, 2, 2, 3, 4, 5]))
print(calculate_standard_deviation([1, 2, 3, 4, 5]))
print(calculate_standard_deviation([1, 2, 3, 4, 5], sample=False))