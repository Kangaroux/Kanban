from user.models import User


def create_user():
  return User.objects.create_user(
    first_name="John",
    last_name="Smith",
    username="jsmith",
    email="test@test.com",
    password="password123"
  )