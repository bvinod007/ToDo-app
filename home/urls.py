from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [
    path('', home, name='home'),
    path('get-todos/', get_todos, name='get-todos'),
    path('post-todo/', post_todo, name='post-todo'),
    path('patch-todo/', patch_todo, name='patch-todo'),
    path('delete-todo/<str:uuid>/', delete_todo, name="delete-todo"),

    path('todos/', TodoViews.as_view())
]

urlpatterns = router.urls