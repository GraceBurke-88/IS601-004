from Calculator import Calculator

""" gnb5 implemented on 2/26/23 
Notes: intitally FAILED test_Calculator.py::test_add - assert 5 == 6.0 --> was converting float to int
Checks the add method for basic addition, floating point addition, and positive/negative addition
"""
#Test number-add-number
def test_add():
    calc = Calculator()
    check = calc.add(3, 2)
    assert check == 5
    assert calc.add(2, -2) == 0
    assert calc.add(2.5, 3.5) == 6.0


""" 
gnb5 implemented on 2/26/23 
tests for adding ans to a value
preloaded ans to be '3'
"""
#Test ans-add-number
def test_add_ans():
    calc = Calculator()
    calc.ans = 3
    assert calc.add("ans", 2) == 5
    assert calc.add("ans", 2) == 7
    assert calc.add("ans", -5) == 2
""" 
gnb5 implemented on 2/26/23 
tests for subtraction of ints/floats and negative values
"""
#Test number-sub-number
def test_sub():
    calc = Calculator()
    assert calc.sub(3, 2) == 1
    assert calc.sub(3.5, 2.25) == 1.25
    assert calc.sub(-10, -2) == -8

""" 
gnb5 implemented on 2/26/23
tests for subtracting a value from ans
preloaded ans to be '3'
"""
#Test ans-sum-number
def test_sub_ans():
    calc = Calculator()
    calc.ans = 3
    assert calc.sub("ans", 2)
    assert calc.sub("ans", -2) == 3
    assert calc.sub("ans", 2) == 1

""" 
gnb5 implemented on 2/26/23 
tests for multiplying int/float/ and negative values

"""
#Test number-mult-number
def test_mult():
    calc = Calculator()
    assert calc.mult(3, 2) == 6
    assert calc.mult(-3, 2) == -6
    assert calc.mult(3.25, 2.50) == 8.125

""" 
gnb5 implemented on 2/26/23 
tests for multiplying ans by inputted value
preloaded ans to be '3'
"""
#Test ans-mult-number
def test_mult_ans():
    calc = Calculator()
    calc.ans = 3
    assert calc.mult("ans", 2) == 6
    assert calc.mult("ans", 2) == 12
    assert calc.mult("ans", 0.5) == 6

""" gnb5 implemented on 2/26/23 
Tests for division method ('div') of integers and floating point values
"""
#Test number-div-number
def test_div():
    calc = Calculator()
    assert calc.div(6, 2) == 3
    assert calc.div(6.5, 2.5) == 2.6

""" 
gnb5 implemented on 2/26/23
Tests dividing ans by an inputted value
preloaded ans to be '15'
"""
#Test ans-div-number
def test_div_ans():
    calc = Calculator()
    calc.ans = 30
    assert calc.div("ans", 2)== 15
    assert calc.div("ans", 3)== 5