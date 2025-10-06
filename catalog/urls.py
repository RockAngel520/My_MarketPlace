from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactsTemplateView, ProductDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='catalog'),
    path('catalog/product_create/', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/product_confirm_delete/', ProductDeleteView.as_view(), name='product_confirm_delete'),
]
