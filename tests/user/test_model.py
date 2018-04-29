from models.user import User


def test_password_field_length():
  """ Tests that the user model has enough room to fit a hashed password """
  u = User()
  u.set_password("mysecretpassword")
  assert User.password.type.length >= len(u.password)

def test_password_match():
  """ Tests a matching password """
  u = User()
  u.set_password("mysecretpassword")
  assert u.check_password("mysecretpassword")

def test_password_nomatch():
  """ Tests an incorrect password """
  u = User()
  u.set_password("mysecretpassword")
  assert not u.check_password("hackerman123")