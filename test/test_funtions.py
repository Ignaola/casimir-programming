from casimir_programming import functions
from math import pi
def test_area():
    assert functions.area(1)==pi
def test_circunference():
    assert functions.circunference(1)==2*pi