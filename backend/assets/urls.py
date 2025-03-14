from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.AssetListView.as_view(), name='asset-list'),
]
