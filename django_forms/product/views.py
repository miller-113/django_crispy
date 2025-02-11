from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
import django_tables2 as tables
from django.utils.html import format_html

from .models import Product
from .forms import ProductForm

class ProductCreateView(FormView):
    template_name = "product/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successful added!")
        return super().form_valid(form)


class ProductTable(tables.Table):
    id = tables.Column(
        verbose_name=format_html('ID <i class="fas fa-sort"></i>'),
        attrs={"th": {"class": "sortable"}}
    )
    name = tables.Column(
        verbose_name=format_html('Name <i class="fas fa-sort"></i>'),
        attrs={"th": {"class": "sortable"}}
    )
    price = tables.Column(
        verbose_name=format_html('Price <i class="fas fa-sort"></i>'),
        attrs={"th": {"class": "sortable"}}
    )

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
