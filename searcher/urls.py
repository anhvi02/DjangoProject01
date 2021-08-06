from django.contrib import admin
from django.urls import include, path
from . import views
app_name = 'searcher'

urlpatterns = [
    path('us/', views.us,name='us_url'),
    path('result/',views.result,name='result_url'),
    path('analytics/', views.analytics,name='analytics_url')
]
