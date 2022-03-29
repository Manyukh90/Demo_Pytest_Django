import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create_1():
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.all().count()
    print(f'--- all user: {count}')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_create_2():
    count = User.objects.all().count()
    print(f'--- all user: {count}')
    assert count == 0 


# # >>> Flow for write test , Arrange > Act > Assert

# # > use fixture create object to db

# Arrange
@pytest.fixture()
def create_user(db):
    print('> Run create_user')
    user = User.objects.create_user('test_user')
    return user 

def test_set_check_password(create_user):
    print('> Run test_set_check_password')
# Act    
    create_user.set_password("test_password")
# Assert    
    assert create_user.check_password('test_password') is True       