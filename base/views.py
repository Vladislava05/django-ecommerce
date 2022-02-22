from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    
    context = {'products':products}
    return render(request, 'base/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'base/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'base/checkout.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'base/product_detail.html'

class SearchResultsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'search.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].filter(user=self.request.user)
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['products'] = context['products'].filter(title__icontains=search_input)
        context['search_input'] = search_input

        return context


