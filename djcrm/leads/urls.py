from django.urls import path

from .views import lead_create, lead_details, lead_list

app_name = 'leads'

urlpatterns = [
    path("", lead_list),
    path('<int:pk>',lead_details),
    path('create/',lead_create),
]
