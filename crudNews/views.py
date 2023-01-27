from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from . serializers import *
from rest_framework import permissions
# Create your views here.
'''CRUD News views'''



'''Yangiliklar yaratish funksiyasi faqat admin foydalana oladi'''
class CreateNewsView(generics.ListCreateAPIView):

	queryset = News.objects.all()
	serializer_class = NewsCreateSerializer
	permission_classes = [permissions.IsAdminUser]

	def post(self,request):

		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():

			serializer.save()
			return Response(serializer.data,status=201)


		return Response(serializer.errors,status=400)

'''Yangiliklarno o'zgartirish ya'ni PUT,READ,DELETE amallarini ichiga olgan
faqat sayt admini quyidagi amallarni bajara oladi

'''
class DetailNewsView(generics.RetrieveUpdateDestroyAPIView):



	serializer_class = DeatilNewsSerializer
	permission_classes = [permissions.IsAdminUser]

	def get_queryset(self):

		pk = self.kwargs['pk']
		try:
			news = News.objects.get(pk=pk)

		except Exception as e:
			news = None

		return news

	def get(self,request,pk):
		query = self.get_queryset()
		serializer = self.serializer_class(query)
		return Response(serializer.data,status=200)


	def put(self,request,pk):

		news = self.get_queryset()
		serializer = self.serializer_class(news,request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=200)

		else:
			return Response(serializer.errors,status=400)


	def delete(self,request,pk):

		news = self.get_queryset()
		news.delete()
		return Response({'Deleted':True})





	

