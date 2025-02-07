from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Product


class BaseCrispyForm(forms.ModelForm):
    submit_label = "Submit"
    form_action = "" 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_action = self.form_action

        self.helper.add_input(Submit("Submit", self.submit_label, css_class="btn btn-dark"))


class ProductForm(BaseCrispyForm):
    class Meta:
        model = Product
        fields = ["name", "quantity", "price"]

    submit_label = "Add Product" 
