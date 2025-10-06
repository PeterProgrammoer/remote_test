import pytest
import u36_07_calculator__program as calc

def xtest_main1():
    # main returnerer intet...
    expected = None
    result = calc.main()
    assert result == expected

def xtest_main2(mocker):
    mocker.patch(
        'u36_07_calculator__program.input',
        return_value="5")
    expected = None
    result = calc.main()
    assert result == expected


def xtest_main3(mocker):
    mocker.patch(
        'u36_07_calculator__program.input',
        return_value="5")
    result = calc.main()
    calc.input.assert_called_with("Number 1  >")
    
def xtest_main4(mocker):
    mocker.patch(
        'u36_07_calculator__program.input',
        return_value="5")
    result = calc.main()
    calc.input.assert_any_call("Number 1  >")
    calc.input.assert_any_call("Operation +-*/  >")
    calc.input.assert_any_call("Number 2  >")
    
    
    
    
    
    


def test_main5(mocker):
    
    mocker.patch('u36_07_calculator__program.input',
        side_effect=["5","+","7"])
    
def xtest_main5(mocker):
    mocker.patch('u36_07_calculator__program.calculate_number')
def xtest_main6(mocker):
    expected = None
def xtest_main7(mocker):
    result = calc.main()
    # assert result == expected
    calc.input.assert_called_once()
    # calc.input.assert_called_with("Number 2  >")
    calc.calculate_number.assert_called_once()
    calc.calculate_number.assert_called_with("5", "5", "5")
    calc.calculate_number.assert_called_with("5", "+", "7")
    
    
    #assert result == expected


def test_addition():
    number1 = 1
    operator = '+'
    number2 = 3
    expected = 4
    result = calc.calculate_number(number1, operator, number2)
    assert result == expected


def test_addition():
    number1 = '1'
    operator = '+'
    number2 = '3'
    expected = 4
    result = calc.calculate_number(number1, operator, number2)
    assert result == expected

def test_addition_num1_float_point():
    number1 = '1.5'
    operator = '+'
    number2 = '3'
    expected = 4.5
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_addition_num1_float_comma():
    number1 = '2,5'
    operator = '+'
    number2 = '3'
    expected = 5.5
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_addition_num1_letter_():
    number1 = 'a'
    operator = '+'
    number2 = '3'
    expected = 'ERROR number input must be a number'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_addition_num2_letter_():
    number1 = '3'
    operator = '+'
    number2 = 'b'
    expected = 'ERROR number input must be a number'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_addition_num2_empty():
    number1 = '3'
    operator = '+'
    number2 = ''
    expected = 'ERROR number input must be a number'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_addition_num2_space():
    number1 = '3'
    operator = '+'
    number2 = ' '
    expected = 'ERROR number input must be a number'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_addition_with_zero():
    number1 = '5'
    operator = '+'
    number2 = '0'
    expected = 5
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_subtraction():
    number1 = '5'
    operator = '-'
    number2 = '3'
    expected = 2
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_subtraction_zero():
    number1 = '5'
    operator = '-'
    number2 = '0'
    expected = 5
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_multiplication():
    number1 = '3'
    operator = '*'
    number2 = '5'
    expected = 15
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_multiplication_zero():
    number1 = '3'
    operator = '*'
    number2 = '0'
    expected = 0
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_division():
    number1 = '8'
    operator = '/'
    number2 = '16'
    expected = 0.5
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_division_by_zero():
    number1 = '8'
    operator = '/'
    number2 = '0'
    expected = 'ERROR cannot divide by zero'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_operation_other():
    number1 = '8'
    operator = 'x'
    number2 = '5'
    expected = 'Unknown operation'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

def test_operation_empty():
    number1 = '8'
    operator = ''
    number2 = '5'
    expected = 'Unknown operation'
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected

@pytest.mark.parametrize(
    "test_parameters",
    [
        pytest.param(['1','+','2',3],id='sum good values'),
        pytest.param(['2','*','3',6], id='mulitply good values'),
    ]
)
def test_operation_param(test_parameters):
    number1,operator,number2,expected = test_parameters
    result = calc.calculate_number(number1,operator,number2)
    assert result == expected



retcode = pytest.main(['-vvrA', __file__])
print(retcode)
