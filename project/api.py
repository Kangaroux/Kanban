from .forms import CreateBoardForm, CreateColumnForm, CreateProjectForm
from .models import Board, Column, Project, Task
from lib.views import APIView, LoginRequiredMixin, MissingError


class ProjectAPI(LoginRequiredMixin, APIView):
  def get(self, request, project_id=None):
    """ Gets a single project by id or a collection of projects """
    if project_id is not None:
      project = self.get_or_404(Project, project_id)
      return self.ok({ "project": project.serialize() })

    # TODO: Add appropriate filtering here
    projects = Project.objects.all()
    return self.ok({ "projects": [ p.serialize() for p in projects ] })

  def post(self, request):
    """ Creates a new project and returns it """
    form = CreateProjectForm(request.POST)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    project = Project.objects.create(
      name=data["name"],
      description=data.get("description"),
      created_by=request.user
    )

    return self.ok({ "project": project.serialize() }, status=201)

  def delete(self, request, project_id):
    """ Deletes a project """
    project = self.get_or_404(Project, project_id)
    project.delete()

    return self.ok()


class BoardAPI(LoginRequiredMixin, APIView):
  def get(self, request, board_id=None):
    """ Gets a single board by id or a collection of boards """
    if board_id is not None:
      board = self.get_or_404(Board, board_id)
      return self.ok({ "board": board.serialize() })

    # TODO: Add appropriate filtering here
    boards = Board.objects.all()
    return self.ok({ "boards": [ b.serialize() for b in boards ] })

  def post(self, request):
    """ Creates a new board and returns it """
    form = CreateBoardForm(request.POST)

    if not form.is_valid():
      return self.form_error(form)

    data = form.cleaned_data
    board = Board.create_board(
      name=data["name"],
      description=data.get("description"),
      created_by=request.user
    )

    return self.ok({ "board": board.serialize() }, status=201)

  def delete(self, request, board_id):
    """ Deletes a board """
    board = self.get_or_404(Board, board_id)
    board.delete()

    return self.ok()


class ColumnAPI(LoginRequiredMixin, APIView):
  def get(self, request, board_id, column_id=None):
    """ Gets a single column by id or a collection of columns """
    board = self.get_or_404(Board, board_id)

    if column_id is not None:
      column = self.get_or_404(Column, column_id)
      return self.ok({ "column": column.serialize() })

    # TODO: Add appropriate filtering here
    return self.ok({ "columns": [ c.serialize() for c in board.get_columns_ordered() ] })

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

    return self.ok({ "column": column.serialize() }, status=201)