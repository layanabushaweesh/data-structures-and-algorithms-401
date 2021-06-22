from challanges.multi_bracket_validation.multimultibracketvalidation import multi_bracket_validation



def test_false():
    exbected = False
    actual = multi_bracket_validation('(](')
    assert actual == exbected

def test_true(): 
    exbected = True
    actual = multi_bracket_validation('()')
    assert actual == exbected


def test_true_1():
    actual = multi_bracket_validation('(){}')
    exbected = True
    assert actual == exbected




def test_true_2():
    actual = multi_bracket_validation('(){}[[()]]')
    exbected = True
    assert actual == exbected


def test_true_3():
    actual = multi_bracket_validation('{}{layan}(())')
    exbected = True
    assert actual == exbected








