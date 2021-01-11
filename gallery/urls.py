from django.urls import path
from django.conf.urls import url

from . import views


urlpatterns = [
    path('',views.welcome,name='home'),
    url(r'^search/', views.search_results, name='search_results')
    # path('dynamic/<slug:query>/' , dynamic_urls, name='dynamic')
]