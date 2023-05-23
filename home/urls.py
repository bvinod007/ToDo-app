from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('get-todos/', views.get_todos, name='get-todos'),
    path('post-todo/', views.post_todo, name='post-todo')
]