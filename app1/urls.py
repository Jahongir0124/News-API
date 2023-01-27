from django.urls import path
from . views import *


urlpatterns = [
	
	path('',DashboardNews.as_view()),#dashboard Views
	path('reverse',RevserseDashboardNews.as_view()),#Reverse views news
	path('byName',FilterByName.as_view()),#Filter news url
	path('search',SearchByName.as_view()),#search view url



]