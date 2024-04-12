# simple app using flask and postman

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to another flask tutorial'

@app.route('/calculate', methods = ["GET"])
def math_operator():
    operation = request.json['operation']
    number1 = request.json['number1']
    number2 = request.json['number2']

    if operation == 'add':
        result = int(number1) + int(number2)
    elif operation == 'subtract':
        result = int(number1) - int(number2)
    elif operation == 'multiply':
        result = int(number1) * int(number2)
    else:
        result = int(number1) / int(number2)
    #return jsonify(result)
    return 'The operation is {} and Result is {}'.format(operation, result)


print(__name__)

if __name__ == '__main__':
    app.run()

