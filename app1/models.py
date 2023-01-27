from django.db import models

# Create your models here.


'''Таблиса новостей--Yangiliklar jadvali'''

class News(models.Model):


	name = models.CharField(max_length=400,verbose_name='Yangilik nomi')
	text = models.TextField(verbose_name='Yangilik matni')
	author = models.CharField(max_length=400,verbose_name='Yangilik muallifi')
	datePublished = models.DateTimeField(auto_now=False,verbose_name='Chiqgan sana')
	dataCreated = models.DateTimeField(auto_now_add=True)
	dataUpdated = models.DateTimeField(auto_now=True)



	def __str__(self):

		return self.name

	class Meta:

		verbose_name = 'Yangilik'
		verbose_name_plural = 'Yangiliklar ro\'yxati'
