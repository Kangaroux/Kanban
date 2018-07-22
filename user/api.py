from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm, LoginForm
from .models import User
from lib.views import APIView, LoginRequiredMixin


class SessionAPI(APIView):
  """ Session API for logging in and logging out """

  def get(self, request):
    data = {
      "logged_in": request.user.is_authenticated
    }

    if request.user.is_authenticated:
      data.update(UserAPI.get_user_data(request.user))

    return self.ok(data=data)

  def post(self, request):
    """ Logs a user in """
    form = LoginForm(request.POST)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    user = authenticate(username=data["email"], password=data["password"])

    if not user:
      return self.error(msg="Email or password is incorrect.")

    login(request, user)

    return self.ok(data={ "user": user.serialize() })

  def delete(self, request):
    """ Logs a user out """
    logout(request)

    return self.ok()


class UserAPI(APIView):
  @staticmethod
  def get_user_data(user):
    """ Serializes the user and returns it as a dict """
    return {
      "user": user.serialize()
    }

  def get(self, request, user_id):
    """ Returns a user's info """
    user = self.get_or_404(User, user_id)

    return self.ok(data=self.get_user_data(user))

  def post(self, request):
    """ Adds a new user """
    form = CreateUserForm(request.POST)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    del data["confirm_password"]

    user = User.objects.create_user(**data)

    return self.ok({ "user": user.serialize() }, status=201)

  # def patch(self, user_id):
  #   """ Updates an existing user """
  #   u = User.get_or_404(user_id)

  #   return self.ok(data={ "user": u.serialize(exclude=["updated"]) })

  def delete(self, request, user_id):
    """ Deletes an existing user """
    if not request.user.is_authenticated:
      return self.not_logged_in()

    user = self.get_or_404(User, user_id)

    if user.id == request.user.id:
      logout(request)

    user.delete()

    return self.ok()