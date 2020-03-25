from rest_framework import serializers

from .models import GStats,State,News

class GStatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GStats
        fields = ['confirmed','deaths','recovered']

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ['name','confirmed','recovered','deaths']

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ['title','content','date']