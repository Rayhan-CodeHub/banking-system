# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('diposit/', views.diposit_data, name='diposit'),
    path('diposit/status/', views.status_display, name='status'),
    path('statement/',views.transactions_statement.as_view(),name='statement'),
]
