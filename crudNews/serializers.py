from rest_framework import serializers
from app1.models import News


'''Create Serializer'''
class NewsCreateSerializer(serializers.ModelSerializer):



	class Meta:
		model = News
		fields = '__all__'


	def create(self,validated_data):

		news = News.objects.create(**validated_data)

		return news


'''Detail Serailizer'''
class DeatilNewsSerializer(serializers.ModelSerializer):


	class Meta:

		model = News
		fields = ("name","author","text")


	def update(self,instance,validated_data):

		instance.name = validated_data['name']
		instance.author = validated_data['author']
		instance.text = validated_data['text']
		instance.save()
		return instance