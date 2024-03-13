import random 

def calculate_income_tax(annual_income):
    if annual_income <=12500:
        return 0
    
    elif annual_income <= 500000:
        return (annual_income -12500)* 0.2
    
    else:
        return 7500 +(annual_income - 500000 ) * 0.4
    
    
def generate_question():
    annual_income = random.randint(100000, 1000000)
    income_tax = calculate_income_tax(annual_income)
    return annual_income , income_tax





def print_solution(annual_income, income_tax):
    print(" Solution:")
    print(f"1. Calculate the taxable income by subtracting the personal allowance (£12,500) from the annual income:")
    print(f"   Taxable Income = Annual Income - Personal Allowance")
    print(f"                   = £{annual_income} - £12,500")
    taxable_income = annual_income - 12500
    print(f"                   = £{taxable_income}")
    print(f"2. Determine the tax rate based on the taxable income:")
    if taxable_income <= 0:
        tax_rate = "0%"
    elif taxable_income <= 37500:
        tax_rate = "20%"
    else:
        tax_rate = "40%"
    print(f"   Tax Rate = {tax_rate}")
    print(f"3. Calculate the income tax by applying the tax rate to the taxable income:")
    print(f"   Income Tax = Taxable Income * Tax Rate")
    income_tax_calculation = taxable_income * 0.2 if taxable_income <= 37500 else 7500 + (taxable_income - 37500) * 0.4
    print(f"               = £{income_tax_calculation}")
    print(f"\nTotal Income Tax for an annual income of £{annual_income} is £{income_tax:.2f}")
   
   

annual_income, income_tax = generate_question()

print(f"What is the income tax for an annual income of £{annual_income}?")
print()

print_solution(annual_income, income_tax)