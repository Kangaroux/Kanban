from .forms import CreateBoardForm, CreateColumnForm
from .models import Board, Column, Task
from lib.views import APIView, LoginRequiredMixin, MissingError


class BoardAPI(LoginRequiredMixin, APIView):
  """ API view for interacting with board objects """

  def get(self, request, board_id=None):
    """ Gets a single board by id or a collection of boards """
    if board_id is not None:
      board = self.get_or_404(Board, board_id)

      return self.ok({ "board": board.serialize() })
    else:
      # TODO: Add appropriate filtering here
      boards = Board.objects.all()

      return self.ok({ "boards": [ b.serialize() for b in boards ] })

  def post(self, request):
    """ Creates a new board and returns its id """
    form = CreateBoardForm(request.POST)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    board = Board.create_board(
        name=data["name"],
        description=data.get("description"),
        owner=request.user,
        created_by=request.user
      )

    return self.ok({ "board_id": board.id }, status=201)

  def delete(self, request, board_id):
    """ Deletes a board """
    board = self.get_or_404(Board, board_id)
    board.delete()

    return self.ok()


class ColumnAPI(LoginRequiredMixin, APIView):
  """ API view for interacting with column objects """

  def post(self, request, board_id):
    """ Adds a new column to a board """
    board = self.get_or_404(Board, board_id)
    form = CreateColumnForm(request.POST, board=board)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    column = Column.create_column(
        name=data["name"],
        board=board
      )

    board.add_column(column, data.get("index"))
    board.save()

    return self.ok({ "column_id": column.id }, status=201)