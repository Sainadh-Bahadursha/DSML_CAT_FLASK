from square import get_square

def test_get_square():
    a = 4
    results = get_square(a)
    assert results == 15
    print("Test case was successfull")

test_get_square()
    
