from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('problem/<int:pk>/', views.problem_detail, name='problem_detail'),
    path('submit/<int:pk>/', views.submit_solution, name='submit_solution'),
    path('submission/<int:pk>/', views.submission_detail, name='submission_detail'),
]
