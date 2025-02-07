from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm

def product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successful added!")
            return redirect("add_product")
    else:
        form = ProductForm()

    return render(request, "product_form.html", {"form": form})
