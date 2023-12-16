from django.urls import path
from . import views

urlpatterns = [
    path("",views.login_page,name="login_page"),
    path("login",views.login_page,name="login_page"),
    path("signup",views.sign,name="sign"),
    path("logout",views.logout_user,name="logout")
]
