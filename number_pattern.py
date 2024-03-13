import random 



def  generate_number_pattern():
    
    
    pattern_type =random.choice(['arithmatic'  , ' geomatric'])
    
    start = random.randint(1,10)
    
    difference =random.randint(1,5)
    
    ratio = random.randint(2,5)
    sequence_lenght = random.randint(5,10)
    
    
    if pattern_type=='arithmatic':
        sequence = [start + i * difference for i in range(sequence_lenght)]
        pattern = f"Arithmetic sequence starting with {start} and difference {difference}"
    else:
        sequence = [start * ratio**i for i in range(sequence_lenght)]
        pattern = f"Geometric sequence starting with {start} and ratio {ratio}"
        
    return sequence , pattern


def solve_number_pattern(sequence):
    deifference = sequence[1] - sequence[0]
    ratio = sequence[1] / sequence[0]
    is_arithmetic = all(sequence[i] - sequence[i-1] == deifference for i in range(1, len(sequence)))
    is_geometric = all(sequence[i] / sequence[i-1] == ratio for i in range(1, len(sequence)))
    
    if is_arithmetic:
        return "Arithmatic sequence with different " +str(deifference)
    elif is_geometric:
        return "Geomatric sequence with ratio  "  +str(ratio)
    
    else:
        return "Not a recognised pattern"
        
sequence , pattern = generate_number_pattern()

solution = solve_number_pattern(sequence)


print("Question: What type of number pattern is represented by the following sequence?")
print("Sequence:", sequence)
print()


print("Solution: ", solution)




# Define a function to generate a random sequence with a specified length.
# Determine the pattern of the sequence.
# Calculate the next number in the sequence based on the determined pattern.
import random

def generate_sequence(length):
    return [random.randint(1, 100) for _ in range(length)]

def determine_sequence_pattern(sequence):
    is_arithmetic = all(sequence[i] - sequence[i-1] == sequence[1] - sequence[0] for i in range(1, len(sequence)))
    ratio = sequence[1] / sequence[0]
    is_geometric = all(sequence[i] / sequence[i-1] == ratio for i in range(1, len(sequence)))
    
    if is_arithmetic:
        pattern = ('arithmetic', sequence[1] - sequence[0])
    elif is_geometric:
        pattern = ('geometric', ratio)
    else:
        pattern = ('random', None)
    
    explanation = f"Sequence: {sequence}\n"
    explanation += f"Arithmetic: {is_arithmetic}\n"
    explanation += f"Geometric: {is_geometric}\n"
    
    return pattern, explanation
    
def generate_next_number(sequence, pattern):
    if pattern[0] == 'arithmetic':
        return sequence[-1] + pattern[1]
    elif pattern[0] == 'geometric':
        return sequence[-1] * pattern[1]
    
sequence = generate_sequence(5)
pattern, explanation = determine_sequence_pattern(sequence)
next_num = generate_next_number(sequence, pattern)

print("Question: What is the next number in the sequence?")
print("Sequence:", sequence)

print("Pattern and Explanation:")
print(explanation)

if next_num is not None:
    print("Solution: The next number in the sequence is", next_num)
else:
    print("The sequence does not follow a recognizable pattern.")

