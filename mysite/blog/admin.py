from django.contrib import admin
from .models import Post

# para fazer operações do banco de dados
admin.site.register(Post)