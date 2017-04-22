from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) #para ficar visivel na administracao
admin.site.register(Comment)
