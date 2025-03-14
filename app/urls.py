from django.shortcuts import render
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    AssetListView,
    CreatorAssetListView,
    AssetUploadView,
    CustomerPurchaseListView,
    PurchaseDetailView,
)

urlpatterns = [
    # Homepage (React container)
    path('home/', AssetListView.as_view(), name='asset-list'),
    
    # Auth pages (using Django's built-in views)
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # For signup, you can create a custom view or use a package like django-registration.
    
    # Creator pages
    path('creator/', CreatorAssetListView.as_view(), name='creator-asset-list'),
    path('creator/upload/', AssetUploadView.as_view(), name='asset-upload'),
    
    # Customer pages
    path('customer/purchases/', CustomerPurchaseListView.as_view(), name='customer-purchase-list'),
    path('customer/purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase-detail'),
    
    # The index page that loads the React app
    path('', lambda request: render(request, "index.html"), name='home-container'),
]
