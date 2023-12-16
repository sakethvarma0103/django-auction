from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="all"),
    path("add",views.add,name="add"),
    path("search",views.search,name="search"),
    path("delete",views.delete,name="delete"),
    path("<slug:slug>",views.detail,name="detail"),
]
