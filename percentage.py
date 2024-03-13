import random


def generate_percentage_problem():
    original_value = random.randint(100, 1000)
    
    percentage_change = random.randint(1,50)
    
    operation= random.choice(['increase', 'decrease'])
    
    
    if operation == 'increase':
        new_value = original_value * (1+ percentage_change/100)
    
    else:
        new_value = original_value * (1- percentage_change/100)
        
    
    problem_statement = f"A {operation} of {percentage_change}% in {original_value} results in what value?"
    
    return original_value, percentage_change, operation, new_value, problem_statement



def print_solution_steps( original_value, percentage_change, operation, new_value):
    print("Solution Steps")
    print(f"step 1 : start with the original value")
    print(f"step 2: Calculate  the change  as a  {operation} of {percentage_change}%.")
    print(f"step 3: Apply the change to  the  original value .")
    
    print(f"        New value = Original value * (1 {'+' if operation == 'increase' else '-'} {percentage_change/100})")
    print(f"                    = {original_value} * (1 {'+' if operation == 'increase' else '-'} {percentage_change/100})")
    print(f"                    = {new_value}")


    
original_value , percentage_change , operation , new_value , problem_statement = generate_percentage_problem()




print("Percentage Problem ")
print(problem_statement)

print()


print_solution_steps(original_value, percentage_change , operation , new_value)