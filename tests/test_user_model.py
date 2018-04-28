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

def test_unique_salt():
  """ Tests that passwords are generated with a new salt """
  u = User()

  u.set_password("secretpass")
  p1 = u.password.split("$")

  u.set_password("secretpass")
  p2 = u.password.split("$")

  # Same algorithm and arguments but different salt and hashes
  assert p1[0] == p2[0]
  assert p1[1] != p2[1]
  assert p1[2] != p2[2]