from django.shortcuts import render
from rest_framework import generics
from .models import GStats,State,News
from .serializers import GStatsSerializer,StateSerializer,NewsSerializer

# Create your views here.
class ListGStatsView(generics.ListAPIView):
    queryset = GStats.objects.all()
    serializer_class = GStatsSerializer


class ListStateView(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class ListNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer