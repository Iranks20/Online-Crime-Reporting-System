from django.urls import path, include
from django.views.generic import TemplateView
from .views import anonymous_tip, anonymous_user_login, anonymous_dashboard, get_interact_anonymous

urlpatterns = [
    path('', anonymous_tip, name='anonymous_tip'),
    path('login/', anonymous_user_login, name='anonymous_user_login'),
    path('dashboard/', anonymous_dashboard, name="anonymous_dashboard"),
]
