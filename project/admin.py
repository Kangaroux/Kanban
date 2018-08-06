from django.contrib import admin
from .models import Board, Column, Project, Task

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Project)
admin.site.register(Task)
