from django.contrib.auth.models import User, Group
from .models import Movies
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields =  '__all__'
