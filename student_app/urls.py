from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name= "homepage"),
    path('numberpattern', views.number_pattern, name= "numberpattern"),
    path('register', views.register_user, name= "register"),
    path('base', views.base)

]
