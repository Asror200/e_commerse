import re
from django import forms
from .models import Comment, Order, Product
from django.contrib.auth.models import User


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


class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords must match.")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Password must contain at least one numbers.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("Password must contain at least one special character.")
        return confirm_password

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
