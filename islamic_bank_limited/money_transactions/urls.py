from django.urls import path
from .templates import views

urlpatterns=[
    path('diposit/',views.entry_data.as_view(),name='diposit'),
    path('status/',views.status_display,name='status'),
    path('statement/',views.transactions_statement.as_view(),name='statement'),
]