from django.urls import path
from .views import get_all, get, create, update, delete

urlpatterns = [
    path('', get_all, name='stickynotes'),
    path('<int:pk>/', get, name='stickynote'),
    path('new/', create, name='create_stickynote'),
    path('<int:pk>/edit/', update, name='update_stickynote'),
    path('<int:pk>/delete/', delete, name='delete_stickynote'),
]
