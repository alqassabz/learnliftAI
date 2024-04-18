from flask_bootstrap import Bootstrap
from flask import Flask, render_template, jsonify, make_response
from add import generate_add_problem
from subtract import generate_sub_problem
from multiply import generate_multi_problem
from divide import generate_div_problem
from findx import generate_find_x_problem, generate_choices
from trig import generate_geometry_question
from general import generate_questions_approach1_with_filtering
from flask import Flask, render_template, request
from quad import generate_find_x_problem_quad, generate_choices_quad



app = Flask(__name__)
Bootstrap(app)


# Custom Jinja2 filter for chr
def jinja2_chr(value):
    return chr(value)

app.jinja_env.filters['chr'] = jinja2_chr

def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start=start)

app.jinja_env.filters['enumerate'] = jinja2_enumerate

# New custom Jinja2 filter
def jinja2_choice_letter(index):
    return chr(ord('A') + index)

app.jinja_env.filters['choice_letter'] = jinja2_choice_letter

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add')
def add():
    # Generate a list of 10 random math problems with multiple-choice options
    math_problems = [generate_add_problem() for _ in range(10)]

    return render_template('add.html', math_problems=math_problems)

@app.route('/multiply')
def multiply():
    # Generate a list of 10 random math problems with multiple-choice options
    math_problems = [generate_multi_problem() for _ in range(10)]

    return render_template('multiply.html', math_problems=math_problems)

@app.route('/findx')
def findx():
    # Generate a new list of 10 random "find x" problems on each request
    find_x_problems = [generate_find_x_problem() for _ in range(10)]

    # Add choices to each problem
    find_x_problems_with_choices = [(problem[0], problem[1], generate_choices(problem[1])) for problem in find_x_problems]

    return render_template('findx.html', find_x_problems_with_choices=find_x_problems_with_choices)

@app.route('/quad')
def quad():
    # Generate a new list of 10 random "find x" problems on each request
    find_x_problems_quad = [generate_find_x_problem_quad() for _ in range(10)]

    # Add choices to each problem
    find_x_problems_with_choices_quad = [(problem[0], problem[1], generate_choices_quad(problem[1])) for problem in find_x_problems_quad]

    return render_template('quad.html', find_x_problems_with_choices=find_x_problems_with_choices_quad)

@app.route('/divide')
def divide():
    # Generate a list of 10 random math problems with multiple-choice options
    math_problems = [generate_div_problem() for _ in range(10)]

    return render_template('divide.html', math_problems=math_problems)

@app.route('/subtract')
def subtract():
    # Generate a list of 10 random math problems with multiple-choice options
    math_problems = [generate_sub_problem() for _ in range(10)]

    return render_template('subtract.html', math_problems=math_problems)



@app.route('/trig')
def trig():
    # Generate geometry question data
    geometry_data = [generate_geometry_question() for _ in range(10)]

    return render_template('trig.html', geometry_questions=geometry_data)

# Route for the general page
@app.route('/general', methods=['GET', 'POST'])
def general_page():
    if request.method == 'POST':
        try:
            user_input_text = request.form['user_input_text']
            generated_questions = generate_questions_approach1_with_filtering(user_input_text)
            return render_template('general.html', generated_questions=generated_questions)
        except KeyError:
            # Handle case where 'user_input_text' is not found in form data
            return "Error: 'user_input_text' not found in form data."
        except Exception as e:
            # Handle other exceptions
            return f"An error occurred: {e}"
    return render_template('general.html')



# Main route
@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)

