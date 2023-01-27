from django.urls import path
from . views import *



urlpatterns = [

	path('create',CreateNewsView.as_view()),# News Post url
	path('detail/<int:pk>/',DetailNewsView.as_view()),#News Detail url
]