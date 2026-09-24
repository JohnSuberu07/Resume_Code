# John Suberu
#This is jus creating functions for the operations
def addition(left, right):
    return left + right 
def subtraction(left, right):
    return left - right
def multiplication(left, right):
    return left * right
def division(left, right): 
    if right == 0:
        return "Error: Division by zero"
    return left / right
def modulus(left, right):
    return left % right
def power(left, right):
    return left ** right
def floor_division(left, right): 
    if right == 0:
        return "Error: Division by zero"
    return left // right
# Here im spilting the expression into 3 parts and writing the function for how it's going to calculate the code
def calculate(expression):
    try: 
        left_str, operator, right_str = expression.split()
        if '.' in left_str or '.' in right_str:
            left = float(left_str)
            right = float(right_str)
        else: left = int(left_str)
        right = int(right_str) 
    
        if operator == '+': 
            return addition(left, right)
        elif operator == '-': 
            return subtraction(left, right)
        elif operator == '*':
            return multiplication(left, right)
        elif operator == '/':
            return division(left, right)
        elif operator == '%':
            return modulus(left, right)
        elif operator == '**':
            return power(left, right)
        elif operator == '//':
            return floor_division(left, right)
        else: return "Error: Invalid operator" 
    except ValueError: return "Error: Invalid expression" 
 
#Here is where I put all the fuctions together and also my input & print statement
while True:
    expression = input("Please enter an Expression: ")
    if expression.lower() in ['quit', 'q']:
        break 
    result = calculate(expression)
    print('Result: ', expression, '= ', result)