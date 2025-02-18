from django.urls import path
from .views import ActivityListView, MarkActivityComplete

urlpatterns = [
    path('activities/<int:day>/', ActivityListView.as_view(), name='activity-list'),
    path('activities/<int:activity_id>/complete/', MarkActivityComplete.as_view(), name='activity-complete'),
]
