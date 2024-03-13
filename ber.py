import random
def calculate_ber(body_mass):
    daily_ber = 5.4 *24 * body_mass
    
    return daily_ber

def print_solution(body_mass, daily_ber):
    print("Solution:")
    print(f"Body mass: {body_mass} kg")
    print("To calculate the Basic Energy Requirement (BER):")
    print("Step 1: Multiply the body mass by 5.4 (the constant for BER calculation)")
    print(f"        = {body_mass} kg * 5.4")
    print(f"        = {5.4 * body_mass} kJ/day")
    print("Step 2: Multiply the result by 24 (hours per day)")
    print(f"        = {5.4 * body_mass} kJ/day * 24")
    print(f"        = {daily_ber} kJ/day")
    print("Therefore, the Basic Energy Requirement (BER) is", daily_ber, "kJ/day")


def main():
    body_mass = random.randint(5, 80)
    
    daily_ber = calculate_ber(body_mass)
    
    print("Problem:")
    print(f"Calculate the Basic Energy Requirement (BER) for a person with a body mass of {body_mass} kg.")
    
    
    print_solution(body_mass , daily_ber)
    
    
if __name__ == "__main__":
    main()