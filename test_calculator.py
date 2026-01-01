import pytest
from calculator import add, divide, subtract

def test_add():
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-12, 15) == 3

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 12) ==  - 2  


def test_divide():
    with pytest.raises(ValueError, match= "cannot divide by zero"):
        divide(10,0)

def test_divide():
    assert divide(10, 2) == 5



#def test_is_even():
#    assert is_even(4) == True

#def test_reverse_string():
#    assert reverse_string("hello") == "olleh"


#def test_get_weather():
#    assert get_weather(21) == "hot"

#assetion simply is going to tell us if something is true or false.


