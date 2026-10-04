
from flask import Flask

app = Flask(__name__)


@app.route('/print/<message>')
def print_message(message):
    return f"Welcome to Calculator API: {message}"

@app.route('/count/<int:num>')
def count(num):
    return "".join(f"<h1>{n}</h1>" for n in range(num + 1))


@app.route('/math/<int:num1>/operation/<operation>/<int:num2>')
def calculator(num1, operation, num2):

    if operation == "+":
        return str(num1 + num2)

    elif operation == "-":
        return str(num1 - num2)

    elif operation == "*":
        return str(num1 * num2)

    elif operation == "%":
        if num2 == 0:
            return "Cannot divide by zero", 400

        return str(num1 % num2)

    else:
        return "Operation not found", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)