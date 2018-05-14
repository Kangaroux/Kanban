from .forms import CreateUserForm, LoginForm
from .models import User
from lib.views import APIView


class AuthAPI(APIView):
  """ Authenticates the user and returns a new session token """

  def post(self):
    """ Validates a user's username and password and returns a new token """
    form = LoginForm()

    if not form.is_valid():
      return self.form_error(form)

    u = User.objects.filter(email=form.email.data).first()

    if not u or not u.check_password(form.password.data):
      return self.error(msg="Email or password is incorrect.", code=http.BAD_REQUEST)

    auth.login(u)

    return self.ok()

  def delete(self):
    was_logged_in = "user_id" in session

    auth.logout()

    return self.ok(data={ "was_logged_in": was_logged_in })


class UserAPI(APIView):
  def get(self, user_id):
    """ Returns a user's info """
    u = User.get_or_404(user_id)

    return self.ok(data={ "user": u.serialize(exclude=["updated"]) })

  def post(self):
    """ Adds a new user """
    form = CreateUserForm()

    if not form.is_valid():
      return self.form_error(form)

    u = User()
    form.populate_obj(u, exclude=["confirm_password", "password"])
    u.set_password(form.data["password"])

    db.session.add(u)
    db.session.commit()

    return self.ok(data={ "user_id": u.id })

  # def patch(self, user_id):
  #   """ Updates an existing user """
  #   u = User.get_or_404(user_id)

  #   return self.ok(data={ "user": u.serialize(exclude=["updated"]) })

  def delete(self, user_id):
    """ Deletes an existing user """
    u = User.get_or_404(user_id)
    delete_self = session["user_id"] == u.id

    db.session.delete(u)
    db.session.commit()

    auth.logout()

    return self.ok()