from django.urls import path,include
from .views import TodoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo',TodoViewSet,basename='todo')

urlpatterns = [
    path('',include(router.urls))
]