from django.contrib.auth.models import User, Group
from rest_framework import serializers
from radiator.models import Alarm


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AlarmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alarm
        fields = ('slug', 'message','description','status','order','date_created','date_updated')
