import random

def generate_question():
    cost_price = random.randint(10, 100)
    profit_or_loss = random.choice(['profit', 'loss'])
    
    if profit_or_loss == 'profit':
        profit_percentage = random.randint(5, 50)
        selling_price = cost_price + (cost_price * profit_percentage / 100) 
    else:
        loss_percentage = random.randint(5, 50)
        selling_price = cost_price - (cost_price * loss_percentage / 100)
        
    return cost_price, selling_price, profit_or_loss

def calculate_profit_loss(cost_price, selling_price, profit_or_loss):
    if profit_or_loss == 'profit':
        profit_or_loss_amount = selling_price - cost_price
    else:
        profit_or_loss_amount = cost_price - selling_price
        
    return profit_or_loss_amount

def calculate_profit_loss_percentage(cost_price, selling_price):
    if selling_price > cost_price:
        profit_percentage = ((selling_price - cost_price) / cost_price) * 100
        return profit_percentage, 'profit'
    elif selling_price < cost_price:
        loss_percentage = ((cost_price - selling_price) / cost_price) * 100
        return loss_percentage, 'loss'
    else:
        return 0, 'No Profit, No Loss'

def get_solution(cost_price, selling_price, profit_or_loss, profit_or_loss_amount):
    print("Question:")
    print(f"If an item is bought at ${cost_price} and then sold for ${selling_price}, calculate the {profit_or_loss}.")
    print("\nSolution:")
    print(f"Cost Price: ${cost_price}")
    print(f"Selling Price: ${selling_price}")
    
    if profit_or_loss_amount != 'percentage':
        print(f"Profit / Loss Amount: ${profit_or_loss_amount}")
        print(f"The transaction resulted in a {profit_or_loss} of ${profit_or_loss_amount}")
    else:
        print(f"The transaction resulted in a {profit_or_loss} of {profit_or_loss_amount:.2f}%")

cost_price, selling_price, profit_or_loss = generate_question()
profit_or_loss_amount = calculate_profit_loss(cost_price, selling_price, profit_or_loss)


if profit_or_loss_amount < 0:
    profit_or_loss_amount = abs(profit_or_loss_amount)
    profit_or_loss_amount, profit_or_loss = calculate_profit_loss_percentage(cost_price, selling_price)
    profit_or_loss_amount = f"{profit_or_loss_amount:.2f}%"

get_solution(cost_price, selling_price, profit_or_loss, profit_or_loss_amount)
calculate_profit_loss_percentage(cost_price , selling_price)