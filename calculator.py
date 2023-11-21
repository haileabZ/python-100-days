

def printer():
    a="""
    +
    -
    *
    /
    """
    print(a)

def num1_receiver():
  return float(input("what's first number?:"))

def num2_receiver():
  return float(input("what's second number?:"))

def operation_picker():
  return input("pick an operation?:")

def calculator(num1,num2,operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2

    
def main():
    global result
    number1=num1_receiver()
    printer()
    operator=operation_picker()
    number2=num2_receiver()
    result = calculator(number1, number2, operator)
    print(number1, operator, number2, "=", result)

if __name__ == '__main__':
    main()



while True:
   prompt=input(f"type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
   if prompt == "y":
       number1=result
       printer()
       operator = operation_picker()
       number2=num2_receiver()
       result = calculator(number1, number2, operator)
       print(number1, operator, number2, "=", result)
   else:
       if __name__ == '__main__':
           main()






