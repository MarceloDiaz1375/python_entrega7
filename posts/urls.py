from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('contacto/', views.contacto, name='contacto'),
    path('posts/<slug:slug>/', views.detalle_post, name='detalle_post'),
    path('post_form/', views.crear_post, name='crear_post'),
    path('post_form/<slug:slug>/', views.editar_post, name='editar_post'),
    path('post_delete/<slug:slug>/', views.eliminar_post, name='eliminar_post'),
]