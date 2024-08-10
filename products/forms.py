from django import forms
from .models import Comment, Order, Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['username', 'phone', 'quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if int(quantity) is None or int(quantity) <= 0:
            raise forms.ValidationError("Quantity must be greater than 0.")
        return quantity


class AddProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class UpdateProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
