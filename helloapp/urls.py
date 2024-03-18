from django.urls import path, include
from .views import hellofunc, HelloClass

urlpatterns = [
    path('hello1/',hellofunc),
    path('hello2/',HelloClass.as_view()),
]
