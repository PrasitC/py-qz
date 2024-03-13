import numpy as np
import math
import random
#linear Equation ---------------------------------
def generate_equation():
    # Generate random coefficients for the equation (ax + b = c)
    a = np.random.randint(-10, 11)  # coefficient 'a' can be any integer from -10 to 10 (inclusive)
    b = np.random.randint(-10, 11)  # coefficient 'b' can be any integer from -10 to 10 (inclusive)
    c = a * np.random.randint(-10, 11) + b  # calculate 'c' based on 'a' and 'b'

    equation = f"{a}x - {b} = {c}"
    return equation, a, b, c
def solve_equation(a, b, c):
    if a == 0:
        return "This is not a linear equation."

    steps = []
    steps.append(f"Given equation: {a}x + {b} = {c}")

    # Step 1: Move 'b' to the other side of the equation
    steps.append(f"Step 1: Subtract {b} from both sides of the equation")
    c -= b
    steps.append(f"        => {a}x = {c}")

    # Step 2: Divide both sides by 'a'
    steps.append(f"Step 2: Divide both sides by {a}")
    x = c / a
    steps.append(f"        => x = {x}")

    return steps

equation, a, b, c = generate_equation()
print("Generated Equation:", equation)

if a == 0:
    print("This is not a linear equation.")
else:
    if a == 1:
        equation = f"x - {b} = {c}"
    elif a == -1:
        equation = f"-x - {b} = {c}"
    else:
        equation = f"{a}x - {b} = {c}"

    print("Simplified Equation:", equation)

    solution_steps = solve_equation(a, b, c)
    for step in solution_steps:
        print(step)


#LCM Equation ---------------------------
import math
import random

def generate_lcm_equation():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    lcm = math.lcm(a, b)
    equation = f"LCM {a} {b} = {lcm}"
    return a, b, lcm, equation

def prime_factorization(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def print_solution_steps(a, b, lcm):
    steps = []
    steps.append(f"Find the prime factors of {a}: {prime_factorization(a)}")
    steps.append(f"Find the prime factors of {b}: {prime_factorization(b)}")
    steps.append("Combine the common prime factors with maximum factors")
    steps.append(f"The Least Common Multiple (LCM) of {a} & {b} is {lcm}")

    print("Solution Steps:")
    for step in steps:
        print(step)

# Generate equation and print solution steps
a, b, lcm, equation = generate_lcm_equation()
print("Generated LCM Equation:", equation)
print_solution_steps(a, b, lcm)


#hCF Equation -----------------------------------


def generate_hcf_equation():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    hcf = math.gcd(a, b)
    equation = f"HCM {a} {b} = {lcm}"
    return a, b, hcf, equation


def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def print_solution_steps(a, b, hcf):
    prime_factors_a = prime_factors(a)
    prime_factors_b = prime_factors(b)
    common_factors = set(prime_factors_a).intersection(prime_factors_b)

    steps = []
    steps.append(f"Find the prime factors of {a}: {prime_factors_a}")
    steps.append(f"Find the prime factors of {b}: {prime_factors_b}")
    steps.append(f"Common prime factors of {a} and {b}: {list(common_factors)}")
    steps.append(f"The Highest Common Factor (HCF) of {a} and {b} is {hcf}")

    print("Solution Steps:")
    for step in steps:
        print(step)

# Generate equation and print solution step
a, b, hcf, equation = generate_hcf_equation()
print("Generated HCF Equation:", equation)
print_solution_steps(a, b, hcf)









