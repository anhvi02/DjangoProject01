from django.contrib import admin
from django.urls import include, path

from searcher import views
urlpatterns = [
    path('', views.home, name='home_url'),
    path('searcher/', include('searcher.urls')),
    path('admin/', admin.site.urls),
]
