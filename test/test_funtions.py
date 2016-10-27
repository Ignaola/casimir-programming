import functions
from math import pi
def test_area():
    assert functions.area(1)==pi
def test_circumference():
    assert functions.circunference(1)==2*pi
    
if __name__== '__main__': 
    test_area()
    test_circumference()
    print('ok')