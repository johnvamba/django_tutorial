from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.CharField(source='get_absolute_url', read_only=True)

	class Meta:
		model = User
		fields = ('url','username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.CharField(source='get_absolute_url', read_only=True)
	class Meta:
		model = Group
		fields = ('url', 'name')