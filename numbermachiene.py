import random
#function for generating random sequencicalt question and random numbers 
def generate_sequene():
    operation = [ '+', '-' , 'x' , '÷' ]
    
    sequence =[]
    
    sequence.append(random.randint(-10, 10))
    
    for _ in range(5):
        sequence.append(random.choice(operation))
        sequence.append(random.randint(1,10))
        
        
    return sequence


def solve_sequence(sequence):
    result = sequence[0]
    steps = [result]
    
    for i in range(1, len(sequence), 2):
        op =sequence[i]
        num = sequence[i+1]
        
        
        if op =='+':
            result +=num
        elif op =='-':
            result -= num
            
        elif op =='x':
            result *= num
            
        elif op =='÷':
            result /=num
            
        steps.append(op)
        steps.append(num)
        steps.append('=')
        steps.append(result)
        
    return result , steps

sequence = generate_sequene()
result , steps = solve_sequence(sequence)

question = "What is the value of INPUT? INPUT = " + " ⇒ ".join(map(str, sequence)) + " = ?"
print("Question:", question)


print("Solution Steps")

for i in range (0, len(steps), 5):
    print(" ".join(map(str, steps[i:i+5])))