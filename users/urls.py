from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload_resume, name='upload'),
    path('logout/', views.logout_view, name='logout'),path('delete/<int:resume_id>/', views.delete_resume, name='delete_resume'),

]