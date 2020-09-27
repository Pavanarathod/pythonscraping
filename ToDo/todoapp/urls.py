from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('todo_d/<int:todo_id>/', views.delete_todo),
]
