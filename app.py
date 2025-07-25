from flask import Flask, render_template, request
import math
import sympy as sp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']

    # Safe evaluation using sympy
    try:
        # Replace ^ with ** for exponentiation
        expression = expression.replace('^', '**')
        # Define mathematical functions and constants
        local_dict = {
            'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan,
            'log': sp.log, 'ln': sp.ln, 'sqrt': sp.sqrt,
            'pi': sp.pi, 'e': sp.E, 'exp': sp.exp
        }
        result = sp.sympify(expression, locals=local_dict).evalf()
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
