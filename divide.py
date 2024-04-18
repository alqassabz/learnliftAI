import random

def generate_div_problem():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    # Set the operator to '+'
    operator = '/'

    correct_answer = calculate_answer(num1, num2)

    # Generate incorrect answer choices
    choices = [correct_answer]
    while len(choices) < 4:
        incorrect_choice = calculate_incorrect_answer(correct_answer)
        if incorrect_choice not in choices:
            choices.append(incorrect_choice)

    # Shuffle the choices
    random.shuffle(choices)

    return f"{num1} {operator} {num2}", correct_answer, choices

def calculate_answer(num1, num2):
    return num1 / num2

def calculate_incorrect_answer(correct_answer):
    # Randomly choose to add or subtract a random value (1 to 5)
    operation = random.choice([lambda x, y: x + y, lambda x, y: x - y])
    return operation(correct_answer, random.randint(1, 5))

# Generate a list of 10 random addition problems with multiple-choice options
addition_problems = [generate_div_problem() for _ in range(10)]

# Print the generated problems, correct answers, and choices
for i, (problem, correct_answer, choices) in enumerate(addition_problems, start=1):
    print(f"Question {i}: {problem}")
    print("Choices:")
    for j, choice in zip("ABCD", choices):  # Use zip to pair choices with A, B, C, D
        print(f"  {j}. {choice}")
    print(f"Correct Answer: {correct_answer}\n")
