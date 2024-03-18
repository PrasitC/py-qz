import random

def gen_bidmas_lvl2():
    # Generate a random integer between 1 and 20
    def random_int():
        num = random.randint(-20, 20)
        while num == 0:
            num = random.randint(-20, 20)
        return num

    # Generate a random operator (+, -, *, /)
    def random_operator():
        return random.choice(['+', '-', '*', '/'])

    # Generate a random indices
    def random_index():
        powers = ["⁰", "¹", "²", "³", "⁴", "⁵"]
        power = random.randint(2,5)
        number = 0
        if power == 2:
            number = random.randint(4, 12)
        elif power == 3:
            number = random.randint(3, 5)
        elif power == 4:
            number = 3
        elif power == 5:
            number = 2
        while len(str(number ** power)) != 2:
            return random_index()
        return {"num":number, "power":power, "pow":powers[power]}

    # Generate a random expression using the BIDMAS rules
    def generate_expression():
        n1 = random_int()
        n2 = random_int()
        while (n1 % n2 != 0) and (n2 != 0) and (n1 != 0) or n2 == 1 or n2 == -1 or (n1 == n2) or (n1 == -n2):
            n1 = random_int()
            n2 = random_int()
        
        op1 = random_operator()
        n3 = random_int()
        op2 = random_operator()
        n4 = random_int()
        op3 = random_operator()
        n5 = random_int()
        op4 = random_operator()
        indices_num = random_index()

        # Logic to generate the expression omitted for brevity
        
        # Return the expression and indices
        return {"n1": n1, "n2": n2, "n3": n3, "n4": n4, "n5": n5, "op1": op1, "op2": op2, "op3": op3, "op4": op4, "indices_num": indices_num}

    # Generate a random expression and its solution steps
    def generate_bidmas_question():
        expr_data = generate_expression()
        n1, n2, n3, n4, n5 = expr_data["n1"], expr_data["n2"], expr_data["n3"], expr_data["n4"], expr_data["n5"]
        op1, op2, op3, op4 = expr_data["op1"], expr_data["op2"], expr_data["op3"], expr_data["op4"]
        indices_num = expr_data["indices_num"]

        # Example solution steps (modify this according to your logic)
        solution_steps = []
        expression = f"{n1} {op1} {n2} {op2} {n3} {op3} {n4} {op4} {n5}"
        solution = eval(expression)
        solution_steps.append(expression)
        solution_steps.append(solution)

        return {"expression": expression, "solution": solution, "solution_steps": solution_steps}

    return generate_bidmas_question()

ques_data = gen_bidmas_lvl2()
print("Expression:", ques_data["expression"])
print("Solution:", ques_data["solution"])
print("Solution Steps:")
for step in ques_data["solution_steps"]:
    print(step)
