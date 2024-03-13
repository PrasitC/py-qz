import random

#Electricity Problem  1 ------------------------------------------

def generate_electricityproblem():
    rate_per_unit = random.uniform(0.05, 0.20)
    total_consumption =random.randint(10,1000)
    problem = f"Rate per unit: ${rate_per_unit:.2f} per kWh\nTotal consumption: {total_consumption} kWh"
    return rate_per_unit, total_consumption, problem


def total(rate_per_unit , total_consumption):
    total_cost = rate_per_unit * total_consumption
    return total_cost

def print_solution_steps(rate_per_unit, total_consumption, total_cost):
    steps = [
        f"Step 1: Multiply the rate per unit (${rate_per_unit:.2f}) by the total consumption ({total_consumption} kWh)",
        f"Step 2: Total Cost = ${rate_per_unit:.2f} * {total_consumption} kWh = ${total_cost:.2f}"
    ]
    for step in steps:
        print(step)
        
rate_per_unit , total_consumption , problem  = generate_electricityproblem()
total_cost = total(rate_per_unit , total_consumption)
    
    
print(" Electricity Problem :")
    
print(problem)
    
print_solution_steps(rate_per_unit, total_consumption, total_cost)





#electricity problem 2 -----------------------------------


def generate_tiered_terrif_problem():
    
    rate_tier1 = random.uniform(0.5 , 0.10)
    rate_tier2 = random.uniform(0.5 , 0.10)
    
    total_consume= random.randint(50, 500)
    
    problem = f"Tiered Tariff Structure\n\nRate for first 100 kWh: ${rate_tier1:.2f} per kWh\nRate for additional kWh: ${rate_tier2:.2f} per kWh\nTotal consumption: {total_consume} kWh"
    return rate_tier1, rate_tier2, total_consume, problem

def total_cost_tt( rate_tier1 , rate_tier2 , total_consume):
    
    if total_consume <= 100:
        total_costing = rate_tier1 * total_consume
        
    else :
        cost_tier1 = rate_tier1*100
        
        additional_consumption = total_consume - 100
        
        cost_additional = additional_consumption * rate_tier2
        
        total_costing = cost_additional + cost_tier1
    return total_costing

def print_solution_tiered_tariff(rate_tier1, rate_tier2, total_consume, total_costing):
    print("Solution Steps:")
    print(f"Step 1: Calculate cost for the first 100 kWh at ${rate_tier1:.2f} per kWh")
    if total_consume > 100:
        print(f"Step 2: Calculate cost for additional {total_consume - 100} kWh at ${rate_tier2:.2f} per kWh")
    print(f"Total Cost = ${total_costing:.2f}")

rate_tier1 , rate_tier2 , total_consume,  problem = generate_tiered_terrif_problem()

total_costing = total_cost_tt( rate_tier1, rate_tier2, total_consume)


print('Electricity Prbolem 2')
print(problem)
print()

print('Solution')

print_solution_tiered_tariff( rate_tier1 , rate_tier2 , total_consume , total_costing )    
    