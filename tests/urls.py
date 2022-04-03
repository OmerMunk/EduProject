from django.urls import path
from . import views

urlpatterns = [
    path('students', views.students),
    path('students/<str:pk>', views.single_student),
    path('tests', views.tests),
    path('test/<str:pk>', views.single_test),
    path('stats', views.stats),
    path('stats/<str:pk>', views.stats_per_student),
]