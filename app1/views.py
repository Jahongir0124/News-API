from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from . serializers import DashboardSerializer
from . models import News
from rest_framework import permissions


'''Dashboard menyusi hamma yangiliklar'''
class DashboardNews(generics.ListAPIView):


	queryset = News.objects.all()
	serializer_class = DashboardSerializer

'''Yaratilgan sana boyicha teskari tartibda chiqarish'''
class RevserseDashboardNews(generics.ListAPIView):

	queryset = News.objects.all().order_by('-datePublished')
	serializer_class = DashboardSerializer

'''Filter By News name'''
class FilterByName(generics.ListAPIView):


	queryset = News.objects.all().order_by('name')
	serializer_class = DashboardSerializer

'''Search name News'''
class SearchByName(generics.ListAPIView):

	serializer_class = DashboardSerializer

	def get_queryset(self):

		name_request = self.request.query_params.get('name')

		news = News.objects.filter(name__icontains=name_request)
		return news

	def get(self,request):

		query = self.get_queryset()
		serializer = self.serializer_class(query,many=True)
		return Response(serializer.data,status=200)


