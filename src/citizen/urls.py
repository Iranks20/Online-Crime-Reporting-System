from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', citizen_logout, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('create_case/', create_case, name='create_case'),
    path('cbcview/<int:sel>/', cbcview, name='cbcview'),
    path('user_case_detail/<int:id>/', user_case_detail, name='user_case_detail'),
    path('create_cyber_case/', create_cyber_case, name='create_cyber_case'),
]
