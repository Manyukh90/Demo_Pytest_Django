import pytest

# >>> Read Me
# -----------------------------
# > A pattern for writing tests
# Stage_01 = Arrange    => prepare date for act stage
# Stage_02 = Act        => call api , read source 
# Stage_03 = Assert     => expect output
# -----------------------------
# > condition scpor fixture
# function      Run once per test
# class         Run once per class of tests
# module        Run once per module
# session       Run once per session
# -----------------------------

# >>>>> fixture do not seesion <<<<<
# it will call fixture_origin() before each test 
# @pytest.fixture
# def fixture_origin():
#     print('---1 Run fixture do not session Set Up ---')
#     return 2

# def test_donot_seesion_example_1(fixture_origin):
#     print('--- Run test_donot_seesion_example_1 ---')
#     num_fixture = fixture_origin
#     assert num_fixture == 2


# def test_donot_seesion_example_2(fixture_origin):
#     print('--- Run test_donot_seesion_example_2 ---')
#     num_fixture = fixture_origin
#     assert num_fixture == 2


# def test_donot_seesion_example_3(fixture_origin):
#     print('--- Run test_donot_seesion_example_3 ---')
#     num_fixture = fixture_origin
#     assert num_fixture == 2 


# >>>>> fixture have seesion <<<<<
# it will call fixture_seesion() once time before every test
# @pytest.fixture(scope='session')
# def fixture_seesion():
#     print('---2 Run fixture_session Set Up ---')
#     return 1


# def test_example_1(fixture_seesion):
#     print('--- Run test_example_1 ---')
#     num_fixture = fixture_seesion
#     assert num_fixture == 1


# def test_example_2(fixture_seesion):
#     print('--- Run test_example_2 ---')
#     num_fixture = fixture_seesion
#     assert num_fixture == 1


# def test_example_3(fixture_seesion):
#     print('--- Run test_example_3 ---')
#     num_fixture = fixture_seesion
#     assert num_fixture == 1 


# >>>>> fixture have suite setup and suit teardown <<<<<
@pytest.fixture
def yield_fixture():
    print('--- Start Test Phase ---')
    yield 6
    print('--- End Test Phase ---')

def test_example_yield(yield_fixture):
    print('--- Run test_example_yield ---')
    assert yield_fixture == 6

