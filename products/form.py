from django import forms
from .models import ProductComment, Order


class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['username', 'email', 'comment']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'username', 'phone']
