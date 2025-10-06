
# DO NOT RUN BEFORE TEST!!
def main():
    number_1 = input('Number 1  >')
    operation = input('Operation +-*/  >')
    number_2 = input('Number 2  >')
    calculate_number(number_1,operation,number_2)
        
def calculate_number(number_1,operation,number_2):
    if number_1.isdigit() == False:
        pass
    if number_1.isdigit() is False:
        pass
    if not number_1.isdigit() or not number_2.isdigit():
        pass
    if not (number_1.isdigit() and number_2.isdigit()):
        pass
    if not (number_1.isnumeric() and number_2.isnumeric()):
        pass
    
    #    return 'ERROR number input must be a number'
    number_1 = number_1.replace(',', '.')
    number_2 = number_2.replace(',', '.')
    try:
        number_1 = float(number_1)
        number_2 = float(number_2)
    except ValueError:
        return 'ERROR number input must be a number'
    
    if operation == '+':
        result = (number_1 + number_2)
    elif operation == '-':
        result = (number_1 - number_2)
    elif operation == '*':
        result = (number_1 * number_2)
    elif operation == '/':
        if number_2 == 0:
            return 'ERROR cannot divide by zero'
        result = (number_1 / number_2)
    else:
        result = 'Unknown operation'
    return result

if __name__ == '__main__':
    main()
