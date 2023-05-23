from django.urls import path
from .views import (
    ClientListCreateView, ClientRetrieveUpdateDestroyView,
    DispatchListCreateView, DispatchRetrieveUpdateDestroyView, DispatchStatsView,
    MessageListCreateView, MessageRetrieveUpdateDestroyView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    path('dispatches/', DispatchListCreateView.as_view(), name='dispatch-list-create'),
    path('dispatches/<int:pk>/', DispatchRetrieveUpdateDestroyView.as_view(), name='dispatch-retrieve-update-destroy'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-retrieve-update-destroy'),
    path('dispatches/stats/', DispatchStatsView.as_view(), name='dispatch-stats'),
]