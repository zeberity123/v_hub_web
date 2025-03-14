from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Asset, Purchase
from .forms import AssetUploadForm

# Main page: Show all assets for customers
class AssetListView(ListView):
    model = Asset
    template_name = "assets/asset_list.html"
    context_object_name = 'assets'
    ordering = ['-uploaded_at']

# Creator's My-Page: List assets uploaded by the logged-in creator
@method_decorator(login_required, name='dispatch')
class CreatorAssetListView(ListView):
    model = Asset
    template_name = "assets/creator_asset_list.html"
    context_object_name = 'assets'

    def get_queryset(self):
        return Asset.objects.filter(creator=self.request.user)

# Asset Upload Page for creators
@method_decorator(login_required, name='dispatch')
class AssetUploadView(CreateView):
    model = Asset
    form_class = AssetUploadForm
    template_name = "assets/asset_upload.html"
    success_url = reverse_lazy('creator-asset-list')

    def form_valid(self, form):
        asset = form.save(commit=False)
        asset.creator = self.request.user
        asset.save()
        return super().form_valid(form)

# Customer's My-Page: List purchase history
@method_decorator(login_required, name='dispatch')
class CustomerPurchaseListView(ListView):
    model = Purchase
    template_name = "purchases/customer_purchase_list.html"
    context_object_name = 'purchases'

    def get_queryset(self):
        return Purchase.objects.filter(customer=self.request.user).order_by('-purchase_date')

# Purchase Detail page: Shows progress and chat messages
@method_decorator(login_required, name='dispatch')
class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = "purchases/purchase_detail.html"
    context_object_name = 'purchase'

# For simplicity, signup/signin pages can use Django's auth views.
# You might add custom views if needed.
