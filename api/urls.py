from .views import ListGStatsView,ListStateView,ListNewsView
from django.urls import path

urlpatterns = [
    path('gstats',ListGStatsView.as_view(),name='global_stats'),
    path('states',ListStateView.as_view(),name='states stats'),
    path('news',ListNewsView.as_view(),name='news')
]