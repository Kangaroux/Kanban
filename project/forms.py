from django import forms

from .models import Board, Column, Task


class BaseBoardForm(forms.ModelForm):
  class Meta:
    model = Board
    fields = ("name", "description", "owner")
