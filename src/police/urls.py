from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='police_dashboard'),
    path('logout/', police_logout, name='police_logout'),
    
    path('cbc/<int:id>/', cbcview, name='cbc'),
    path('cybercbc/<int:id>/', cybercbcview, name='cybercbc'),
    
    path('ajax/get_category/', get_case_categories, name="get_categories"),
    
    path('case_detail/<int:id>/<int:approved>/', case_detail, name='case_detail'),
    
    path('create_criminal_details/', create_criminal_details, name='create_criminal_details'),
    
    path('atips/', atips, name='atips'),
    path('atip_detail/<int:id>/', atip_detail, name='atip_detail'),
]
