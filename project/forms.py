from django import forms

from .models import Board, Column, Project,Task


class BaseProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ("name", "description")


class CreateProjectForm(BaseProjectForm):
  pass


class BaseBoardForm(forms.ModelForm):
  class Meta:
    model = Board
    fields = ("name", "description")


class CreateBoardForm(BaseBoardForm):
  pass


class BaseColumnForm(forms.ModelForm):
  class Meta:
    model = Column
    fields = ("name", "index")

  # The index where this column will be inserted. By default, the column
  # is inserted at the end
  index = forms.IntegerField(required=False)

  def __init__(self, *args, **kwargs):
    self.board = kwargs.pop("board")
    super().__init__(*args, **kwargs)

  def clean_index(self):
    data = self.cleaned_data.get("index")

    if data is not None:
      if data < 0:
        raise forms.ValidationError("Index must be a positive number.")
      elif data > len(self.board.column_order):
        raise forms.ValidationError("Index is too big (max is %d)"
          % len(self.board.column_order))

    return data


class CreateColumnForm(BaseColumnForm):
  pass