from django.contrib.auth.models import User, Group
from rest_framework import serializers
from polls.models import PictureObject

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PictureObject
        fields = ('title', 'source', 'text', 'tags1', 'gender', 'date', 'picture')