from .forms import CreateBoardForm, CreateColumnForm, CreateProjectForm
from .models import Board, Column, Project, Task
from lib.views import APIView, LoginRequiredMixin, MissingError


class ProjectAPI(LoginRequiredMixin, APIView):
  def get(self, request, project_id=None):
    """ Gets a single project by id or a collection of projects """
    if project_id is not None:
      project = self.get_or_404(Project, project_id)
      boards = Board.objects.filter(project=project).only("id")

      data = { "project": Project.serialize(project) }
      data["project"]["boards"] = [ board.id for board in boards ]

      return self.ok(data)

    # TODO: Add appropriate filtering here
    projects = Project.objects.all()
    boards = Board.objects.filter(project__in=projects).only("id", "project_id")
    data = { "projects": Project.serialize(projects) }

    for project in data["projects"]:
      project["boards"] = []

    for board in boards:
      data["projects"][board.project_id]["boards"].append(board.id)

    return self.ok(data)

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

    project.members.set([ request.user ])

    return self.ok({ "project": Project.serialize(project) }, status=201)

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
      return self.ok({ "board": Board.serialize(board) })

    # TODO: Add appropriate filtering here
    boards = Board.objects.all()
    return self.ok({ "boards": Board.serialize(boards) })

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

    return self.ok({ "board": Board.serialize(board) }, status=201)

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
      return self.ok({ "column": Column.serialize(column) })

    # TODO: Add appropriate filtering here
    columns = Column.objects.filter(board=board)
    return self.ok({ "columns": Column.serialize(columns) })

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

    return self.ok({ "column": Column.serialize(column) }, status=201)