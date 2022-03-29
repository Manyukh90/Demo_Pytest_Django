import pytest

def func(x):
    return x + 1


def test_answer_1():
    print('---test_answer_1---')
    assert func(3) == 3

@pytest.mark.skip
def test_answer_2():
    print('---test_answer_2---')
    assert func(3) == 4

@pytest.mark.xfail
def test_answer_3():
    print('---test_answer_3---')
    assert func(3) == 3   

@pytest.mark.slow # tab run by "pytest -x -rP -m 'slow'"
def test_answer_4():
    print('---test_answer_4---')
    assert func(3) == 4       
    