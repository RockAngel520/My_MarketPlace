from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog.html'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

