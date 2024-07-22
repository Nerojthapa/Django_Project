from django.forms import ModelForm
from . models import *
from .models import Category

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"        