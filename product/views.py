from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import ProductForm


class ProductCreateView(FormView):
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("add_product")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Successful added!")
        return super().form_valid(form)
