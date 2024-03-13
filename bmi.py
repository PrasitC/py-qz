import random



def generate_bmi_problem():
    weight = random.randint(40,120)
    height = random.randint(140,200) /100
    
    
    bmi = weight / height ** 2
    bmi_category = get_bmi_category(bmi)
    
    problem = f"A person weighs {weight} kilograms and is {height * 100} centimeters tall. Calculate the BMI (Body Mass Index) of the person and determine their BMI category."
    solution = f"BMI = weight (kg) / height^2 (m^2)\nBMI = {weight} / ({height}^2) = {bmi:.2f}\nBMI Category: {bmi_category}"

    return problem, solution


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
    
problem , solution = generate_bmi_problem()

print("problem")
print(problem)
print()

print("solution")
print(solution)

