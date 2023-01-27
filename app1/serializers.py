from rest_framework import serializers
from . models import News


'''dashboard serializer'''
class DashboardSerializer(serializers.ModelSerializer):


	class Meta:

		model = News
		fields = ("name","text","author","datePublished")
