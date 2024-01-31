from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TodoListViewSet

router = DefaultRouter()
router.register(r'todos', TodoListViewSet, basename='todo-item')


urlpatterns = [
    # path('', views.view_name, name="view_name"),
    path('', include(router.urls)),

]