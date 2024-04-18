import random
import math

def generate_find_x_problem_quad():
    a = random.randint(1, 5)
    b = random.randint(-5, 5)
    c = random.randint(-5, 5)

    # Ensure that b^2 - 4ac is non-negative to have real roots
    while b**2 - 4*a*c < 0:
        a = random.randint(1, 5)
        b = random.randint(-5, 5)
        c = random.randint(-5, 5)

    equation = f"{a}x^2 + {b}x + {c} = 0"
    return equation, calculate_x_values(a, b, c)

def calculate_x_values(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
        root = -b / (2*a)
        return [root]
    else:
        roots = [(-b + math.sqrt(discriminant)) / (2*a),
                 (-b - math.sqrt(discriminant)) / (2*a)]
        return roots

def generate_choices_quad(correct_values):
    choices = []
    correct_option = correct_values.copy()
    random.shuffle(correct_option)
    choices.append(correct_option)
    while len(choices) < 4:
        root1 = round(random.uniform(-5, 5), 2)
        root2 = round(random.uniform(-5, 5), 2)
        if [root1, root2] != correct_values:
            choices.append([root1, root2])
    random.shuffle(choices)
    return choices




# Generate a list of 10 random "find x" problems
find_x_problems = [generate_find_x_problem_quad() for _ in range(10)]

# Print the generated problems and x values
for i, (problem, x_values) in enumerate(find_x_problems, start=1):
    print(f"Question {i}: {problem}")

    # Generate multiple-choice options for some questions
    if random.choice([True, False]):
        choices = generate_choices_quad(x_values)
        print("Choices:")
        for j, choice in enumerate(choices, start=1):
            print(f"  {j}. {choice}")

    formatted_x_values = [int(x) if x.is_integer() else round(x, 2) for x in x_values]
    print(f"Values of x: {formatted_x_values}\n")
