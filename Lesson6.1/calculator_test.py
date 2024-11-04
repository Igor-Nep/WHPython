import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize('num1, num2, result', [(4,5,9), (-6,-10,-16)])
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1,num2)
    assert res == result

def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4,5)
    assert res == 1

def test_sumpositive_negative_nums():
    calculator = Calculator()
    res = calculator.sum(4,-4)
    assert res == 0

def test_sum_float_nums():
    calculcaltor = Calculator()
    res = calculator.sum(5.5, 5.5)
    res = round(res,1)
    assert res == 11

def test_div_pos():
    calculator = Calculator()
    res = calculator.div(4,4)
    assert res == 1

def test_div_byz():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(4,0)
    
def test_avg_el():
    calculator = Calculator()
    nums=[]
    res = calculator.avg(nums)
    assert res == 0
# print('start')
# res = calculator.sum(4,5)
# assert res == 9

# res = calculator.sum(-6, -10)
# assert res == -16

# res = calculator.sum(5.6, 4.3)
# res = round(res, 1)
# assert res == 9.9

# res = calculator.sum(10,0)
# assert res == 10

# res = calculator.div(10, 2)
# assert res == 5

# numbers = []
# res = calculator.avg(numbers)
# assert res == 0

# numbers = [1,2,3,4,5,6,7,8,9,5]
# res = calculator.avg(numbers)
# assert res == 5

# #res = calculator.div(10,0)
# #assert res == None

# print('fin')