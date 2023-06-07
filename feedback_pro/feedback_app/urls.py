from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = 'feedback_app'

urlpatterns = [
    
    # path('', views.index, name='welcome'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    # path('admin_pr/', views.admin_profile, name='admin_pr')
]