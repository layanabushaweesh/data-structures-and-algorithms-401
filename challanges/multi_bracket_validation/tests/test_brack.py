from challanges.multi_bracket_validation.multimultibracketvalidation import multi_bracket_validation



def test_true():
    exbected = True
    actual = multi_bracket_validation('{}')
    assert actual == exbected

def test_true_0(): 
    exbected = True
    actual = multi_bracket_validation('{}(){}')
    assert actual == exbected


def test_true_1():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    exbected = True
    assert actual == exbected




def test_true_2():
    actual = multi_bracket_validation('{}{Code}[Fellows](())')
    exbected = True
    assert actual == exbected


def test_false_3():
    actual = multi_bracket_validation('[({}]')
    exbected = False
    assert actual == exbected

def test_false_4():
    actual = multi_bracket_validation('(](')
    exbected = False
    assert actual == exbected

def test_false_5():
    actual = multi_bracket_validation('{(})')
    exbected = False
    assert actual == exbected










