import random

def generate_find_x_problem():
    coefficient = random.randint(1, 5)
    constant = random.randint(1, 5)
    operator1 = random.choice(['+', '-', '*', '/'])
    operator2 = random.choice(['+', '-'])

    # Equation: coefficient * x operator1 constant operator2 constant = 0
    equation = f"{coefficient}x {operator1} {constant} {operator2} {constant} = 0"
    return equation, calculate_x_value(coefficient, constant, operator1, operator2)


def calculate_x_value(coefficient, constant, operator1, operator2):
    if operator1 == '+':
        if operator2 == '+':
            return (-constant - constant) / coefficient
        elif operator2 == '-':
            return (-constant + constant) / coefficient
        elif operator2 == '*':
            return (-constant / constant) / coefficient
        elif operator2 == '/':
            return (-constant * constant) / coefficient
    elif operator1 == '-':
        if operator2 == '+':
            return (constant - constant) / coefficient
        elif operator2 == '-':
            return (constant + constant) / coefficient
        elif operator2 == '*':
            return (constant / constant) / coefficient
        elif operator2 == '/':
            return (constant * constant) / coefficient
    elif operator1 == '*':
        if operator2 == '+':
            return (-constant - constant) / coefficient
        elif operator2 == '-':
            return (-constant + constant) / coefficient
        elif operator2 == '*':
            return (-constant * constant) / coefficient
        elif operator2 == '/':
            return (-constant / constant) / coefficient
    elif operator1 == '/':
        if operator2 == '+':
            return (constant + constant) / coefficient
        elif operator2 == '-':
            return (constant - constant) / coefficient
        elif operator2 == '*':
            return (constant * constant) / coefficient
        elif operator2 == '/':
            return (constant / constant) / coefficient


def generate_choices(correct_value):
    choices = [correct_value]
    while len(choices) < 4:
        incorrect_choice = round(correct_value + random.uniform(-5, 5), 2)
        if incorrect_choice not in choices:
            choices.append(incorrect_choice)
    random.shuffle(choices)
    return choices


# Generate a list of 10 random "find x" problems
find_x_problems = [generate_find_x_problem() for _ in range(10)]

# Print the generated problems and x values
for i, (problem, x_value) in enumerate(find_x_problems, start=1):
    print(f"Question {i}: {problem}")

    # Generate multiple-choice options for some questions
    if random.choice([True, False]):
        choices = generate_choices(x_value)
        print("Choices:")
        for j, choice in enumerate(choices, start=1):
            print(f"  {j}. {choice}")

    formatted_x_value = int(x_value) if x_value.is_integer() else x_value
    print(f"Value of x: {formatted_x_value}\n")
