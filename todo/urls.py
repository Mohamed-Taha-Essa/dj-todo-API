
from django.urls import path ,include
from rest_framework.routers import DefaultRouter 
from . api import ToDoViewSets

router = DefaultRouter()
router.register('',ToDoViewSets)

urlpatterns = [
    path('todo' ,include(router.urls))
]
