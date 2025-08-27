import calculator

def test_add():
    assert calculator.add(5, 6) == 11

def test_subtract():
    assert calculator.subtract(10, 5) == 5 

def test_multiply():
    assert calculator.multiply(3, 4) == 1

def test_divide():
    assert calculator.divide(10, 2) == 5.0
