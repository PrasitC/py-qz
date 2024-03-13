import random

def generate_seq():
    pos = random.randint(2, 3)
    question = ""
    number = 0
    solution_steps = []

    if pos == 2:
        number = random.randint(3, 12)
        if number == 10:
            return generate_seq()

        question = f"What is {number}²?"
        index_string = "²"
        right_answer = number ** 2
        solution_steps.append(f"Step 1: Square {number}: {number}² = {right_answer}")

    if pos == 3:
        number = random.randint(2, 5)
        question = f"What is {number}³?"
        index_string = "³"
        right_answer = number ** 3
        solution_steps.append(f"Step 1: Cube {number}: {number}³ = {right_answer}")

    return question, right_answer, solution_steps


question, right_answer, solution_steps = generate_seq()


print("Question:", question)


print("Solution Steps:")
for step in solution_steps:
    print(step)


print("Right Answer:", right_answer)
