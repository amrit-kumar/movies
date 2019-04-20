from django.contrib.auth.models import User, Group
from .models import Movies,User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields =  '__all__'
