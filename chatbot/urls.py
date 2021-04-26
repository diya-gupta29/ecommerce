from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('',views.homeView,name='home'),
    path('get_response/',views.get_response,name='get_response'),
]