from django.urls import path

from .views import LeadCrateView, LeadDeleteView, LeadDetailView, LeadListView, LeadUpdateView

app_name = 'leads'

urlpatterns = [
    path("", LeadListView.as_view() , name="lead-list"),
    path('<int:pk>', LeadDetailView.as_view(), name='lead-details'),
    path('<int:pk>/update',LeadUpdateView.as_view(),name='lead-update'),
    path('<int:pk>/delete',LeadDeleteView.as_view(),name='lead-delete'),
    path('create/', LeadCrateView.as_view(),name='lead-create'),
]
