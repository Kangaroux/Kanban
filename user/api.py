from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm, LoginForm
from .models import User
from lib.views import APIView


class AuthAPI(APIView):
  """ Authenticates the user """

  def post(self, request):
    """ Logs a user in """
    form = LoginForm(request.POST)

    if not form.is_valid():
      return self.form_error(form.errors)

    data = form.cleaned_data
    user = authenticate(email=data["email"], password=data["password"])

    if not user:
      return self.error(msg="Email or password is incorrect.", code=http.BAD_REQUEST)

    login(request, user)

    return self.ok()

  def delete(self, request):
    """ Logs a user out """
    logout(request)

    return self.ok()


class UserAPI(APIView):
  def user_does_not_exist(self):
    return self.error("User does not exist.")

  def get(self, request, user_id):
    """ Returns a user's info """
    try:
      user = User.objects.get(id=user_id)
    except User.DoesNotExist:
      return self.user_does_not_exist()

    return self.ok(data={ "user": u.serialize(exclude=["updated"]) })

  def post(self, request):
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

  def delete(self, request, user_id):
    """ Deletes an existing user """
    u = User.get_or_404(user_id)
    delete_self = session["user_id"] == u.id

    db.session.delete(u)
    db.session.commit()

    auth.logout()

    return self.ok()