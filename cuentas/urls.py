from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registro/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),

    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
    path(
        "password/cambiar/",
        auth_views.PasswordChangeView.as_view(
            template_name="registro/password_change.html",
            success_url=reverse_lazy("password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "password/cambiada/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="registro/password_change_done.html"
        ),
        name="password_change_done",
    ),
]