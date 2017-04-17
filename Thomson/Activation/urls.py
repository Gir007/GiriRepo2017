from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^index/', views.first ,name='first'),
    url(r'order/',views.order),
url(r'^connection/',views.login),

]
