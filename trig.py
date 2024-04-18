import random
import math

def generate_geometry_question():
    question_type = random.choice(['area', 'perimeter', 'volume', 'parameter', 'trigonometry'])

    # Define units for variety
    length_units = ['meters', 'centimeters', 'kilometers', 'millimeters', 'inches']
    volume_units = ['cubic meters', 'liters', 'milliliters', 'gallons']

    if question_type == 'area':
        shape = random.choice(['rectangle', 'circle', 'triangle'])
        length_unit = random.choice(length_units)
        length = random.uniform(1, 20)

        if shape == 'rectangle':
            width = random.uniform(1, 20)
            correct_answer = length * width
            choices = generate_choices(correct_answer)
            question = f"What is the area of a rectangle with length {length:.2f} {length_unit} and width {width:.2f} {length_unit}?"
            return question, correct_answer, choices
        elif shape == 'circle':
            radius = random.uniform(1, 15)
            correct_answer = 3.14 * radius ** 2
            choices = generate_choices(correct_answer)
            question = f"What is the area of a circle with radius {radius:.2f} {length_unit}?"
            return question, correct_answer, choices
        elif shape == 'triangle':
            base = random.uniform(1, 15)
            height = random.uniform(1, 15)
            correct_answer = 0.5 * base * height
            choices = generate_choices(correct_answer)
            question = f"What is the area of a triangle with base {base:.2f} {length_unit} and height {height:.2f} {length_unit}?"
            return question, correct_answer, choices

    elif question_type == 'trigonometry':
        trig_function = random.choice(['sine', 'cosine', 'tangent'])
        angle = random.randint(1, 90)
        length_unit = random.choice(length_units)
        side_length = random.uniform(1, 20)

        if trig_function == 'sine':
            hypotenuse = math.sqrt(side_length ** 2 + random.uniform(1, 20) ** 2)
            correct_answer = math.sin(math.radians(angle)) * hypotenuse
            choices = generate_choices(correct_answer)
            question = f"In a right-angled triangle, find the length of the opposite side given an angle of {angle} degrees and a hypotenuse of {hypotenuse:.2f} {length_unit}."
            return question, correct_answer, choices
        elif trig_function == 'cosine':
            hypotenuse = math.sqrt(side_length ** 2 + random.uniform(1, 20) ** 2)
            correct_answer = math.cos(math.radians(angle)) * hypotenuse
            choices = generate_choices(correct_answer)
            question = f"In a right-angled triangle, find the length of the adjacent side given an angle of {angle} degrees and a hypotenuse of {hypotenuse:.2f} {length_unit}."
            return question, correct_answer, choices
        elif trig_function == 'tangent':
            correct_answer = math.tan(math.radians(angle)) * side_length
            choices = generate_choices(correct_answer)
            question = f"In a right-angled triangle, find the length of the opposite side given an angle of {angle} degrees and the adjacent side is {side_length:.2f} {length_unit}."
            return question, correct_answer, choices

    # If no valid question was generated, recursively try again
    return generate_geometry_question()

# Add the generate_choices function if it's not already present in the file
def generate_choices(correct_answer):
    choices = [correct_answer]
    while len(choices) < 4:
        deviation = random.uniform(0.1, 0.5) * correct_answer
        incorrect_answer = correct_answer + deviation if random.choice([True, False]) else correct_answer - deviation
        if incorrect_answer not in choices:
            choices.append(incorrect_answer)
    random.shuffle(choices)
    return choices
