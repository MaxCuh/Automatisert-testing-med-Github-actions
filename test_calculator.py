import pytest 
from calculator import add, subtract, multiply, divide 
 
def test_add(): 
    """Test at addisjon fungerer""" 
    assert add(2, 3) == 5 
    assert add(-1, 1) == 0 
    assert add(0, 0) == 0 
 
def test_subtract(): 
    """Test at subtraksjon fungerer""" 
    assert subtract(5, 3) == 2 
    assert subtract(0, 5) == -5 
 
def test_multiply(): 
    """Test at multiplikasjon fungerer""" 
    assert multiply(3, 4) == 12 
    assert multiply(-2, 3) == -6 
 
def test_divide(): 
    """Test at divisjon fungerer""" 
    assert divide(10, 2) == 5 
    assert divide(9, 3) == 3 
 
def test_divide_by_zero(): 
    """Test at divisjon med null gir feilmelding""" 
    with pytest.raises(ValueError): 
        divide(10, 0) 

 