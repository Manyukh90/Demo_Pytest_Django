from django.contrib.auth.models import User

# >>>   refacturing function test
# >>>   import from conftest.py

# ----- function ref 001 -----

def test_set_check_user_01(create_user):
    print('> Run test_set_check_user_01')
    assert create_user.username == 'test_user' 


def test_set_check_user_02(create_user):
    print('> Run test_set_check_user_02')
    assert create_user.username == 'test_user'



# ----- function ref 002 -----

def test_new_user(new_user):
    print('> run test_new_user')
    user_name           = new_user.username
    first_name          = new_user.first_name
    last_name           = new_user.last_name 
    assert user_name    == 'Test_User'
    assert first_name   == 'Test_First_Name'
    assert last_name    == 'Test_Last_Name'


def test_new_staff_user(new_staff_user):
    print('> run test_new_staff_user')
    user_name           = new_staff_user.username
    first_name          = new_staff_user.first_name 
    assert user_name    == 'Test_User'
    assert first_name   == 'Test_First_Name'
    assert new_staff_user.is_staff       