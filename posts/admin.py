from django.contrib import admin
from .models import Post

# Register your models here.
#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'autor', 'fecha_creacion', 'estado')
    search_fields = ('titulo', 'contenido', 'autor')
    list_filter = ('fecha_creacion', 'estado', 'autor')
    prepopulated_fields = {'slug': ('titulo',)}