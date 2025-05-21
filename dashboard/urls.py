from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("problems/", views.problems_list, name="problems_list"),
    path("submissions/", views.my_submissions, name="my_submissions"),
]
