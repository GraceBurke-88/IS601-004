from Calculator import Calculator

""" gnb5 implemented on 2/26/23 """
#Test number-add-number
def test_add():
    calc = Calculator()
    check = calc.add(3, 2)
    assert check == 5
    assert calc.add(2, -2) == 0
    assert calc.add(2.5, 3.5) == 6.0
#FAILED test_Calculator.py::test_add - assert 5 == 6.0

""" gnb5 implemented on 2/26/23 """
#Test ans-add-number
def test_add_ans():
    calc = Calculator()
    calc.ans = 3
    assert calc.add("ans", 2) == 5

""" gnb5 implemented on 2/26/23 """
#Test number-sub-number
def test_sub():
    calc = Calculator()
    assert calc.sub(3, 2) == 1
    assert calc.sub(3.5, 2.25) == 1.25

""" gnb5 implemented on 2/26/23 """
#Test ans-sum-number
def test_sub_ans():
    calc = Calculator()
    calc.ans = 3
    result = calc.sub("ans", 2)
    assert result == 1

""" gnb5 implemented on 2/26/23 """
#Test number-mult-number
def test_mult():
    calc = Calculator()
    assert calc.mult(3, 2) == 6
    assert calc.mult(-3, 2) == -6
    assert calc.mult(3.25, 2.50) == 8.125

""" gnb5 implemented on 2/26/23 """
#Test ans-mult-number
def test_mult_ans():
    calc = Calculator()
    calc.ans = 3
    assert calc.mult("ans", 2) == 6

""" gnb5 implemented on 2/26/23 """
#Test number-div-number
def test_div():
    calc = Calculator()
    assert calc.div(6, 2) == 3
    assert calc.div(6.5, 2.5) == 2.6

""" gnb5 implemented on 2/26/23 """
#Test ans-div-number
def test_div_ans():
    calc = Calculator()
    calc.ans = 6
    result = calc.div("ans", 2)
    assert result == 3