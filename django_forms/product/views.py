from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import ProductForm
import django_tables2 as tables
from .models import Product


class ProductCreateView(FormView):
    template_name = "product/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successful added!")
        return super().form_valid(form)


class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"
        attrs = {
            "class": "table table-bordered table-striped",
            "id": "productTable"
        }
        thead_attrs = {"class": "table-dark"}
        order_by = "id"


class ProductListView(tables.SingleTableView):
    table_class = ProductTable
    model = Product
    template_name = "product/product_list.html"
