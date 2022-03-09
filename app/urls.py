from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('index', views.index),
    path('add', views.add),
    path('tarea/done/<int:id>', views.done),
    path('tarea/edit/<int:id>', views.edit),
    path('tarea/ver/<int:id>', views.ver),
    
]
