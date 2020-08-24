from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('publish', views.publish, name='publish'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]
