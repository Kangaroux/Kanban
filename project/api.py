from .forms import CreateBoardForm
from .models import Board, Column, Task
from lib.views import APIView, LoginRequiredMixin


class BoardAPI(LoginRequiredMixin, APIView):
  def post(self, request):
    form = CreateBoardForm(request.POST)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    board = Board.objects.create(
        name=data["name"],
        description=data.get("description"),
        owner=request.user,
        created_by=request.user
      )

    return self.ok({ "board_id": board.id }, status=201)