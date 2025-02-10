from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import ProductForm
from django.views.generic import ListView
from .models import Product

class ProductCreateView(FormView):
    template_name = "product/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successful added!")
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"
