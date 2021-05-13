
from django.urls import path,include
from .views import index
app_name = "pics"
urlpatterns = [
    path('',index, name='index')
]
