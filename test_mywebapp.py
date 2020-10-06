'''
Using pytest we are testing
'''

from mywebapp import indexpage

def test_indexpage():
    assert indexpage() == "Wel Come"
