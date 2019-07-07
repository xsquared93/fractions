import fractions

def tests():
    exp = 2, '/', 3
    assert add_rat(exp, exp) == (12, '/', 9)

    assert sub_rat(exp, exp) == (0, '/', 9)

    assert mul_rat(exp, exp) == (4, '/', 9)

    assert div_rat(exp, exp) == (6, '/', 6)

    return 'pass'

tests()
