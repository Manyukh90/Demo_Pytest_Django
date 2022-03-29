import pytest
from django.contrib.auth.models import User


#>>> This Set Up will run before each test ref 001
@pytest.fixture
def create_user(db):
    user = User.objects.create_user('test_user')
    print('> create_user do not use factory')
    return user 


# #>>> This Set Up will generate data for every test ref 002
@pytest.fixture
def new_user_factory(db):
    def create_app_user(
        username    : str,
        password    : str = None,
        first_name  : str = 'firstname',
        last_name   : str = 'lastname',
        email       : str = 'test@test.com',
        is_staff    : str = False,
        is_superuser: str = False,
        is_active   : str = True,     
    ):
        user = User.objects.create_user(
            username    =username,
            password    =password,
            first_name  =first_name,
            last_name   =last_name,
            email       =email,
            is_staff    =is_staff,
            is_superuser=is_superuser,
            is_active   =is_active,
        )
        return user
    return create_app_user



@pytest.fixture
def new_user(db, new_user_factory):
    print('> create new_user')
    new_user = new_user_factory(username='Test_User', first_name= 'Test_First_Name', 
    last_name= 'Test_Last_Name')
    return new_user


@pytest.fixture
def new_staff_user(db, new_user_factory):
    print('> create new_staff')
    new_staff_user = new_user_factory(username='Test_User', first_name= 'Test_First_Name', is_staff= True)
    return new_staff_user