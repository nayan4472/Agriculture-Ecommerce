from .models import *
from django import forms

class signupForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = ["user","email","pass1","pass2"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = "__all__"

class addItemsForm(forms.ModelForm):
    class Meta:
        model = addItems
        fields = ["iid","item_image","item_name","price","category","dis"]

class addCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["iid","user","img","name","price"]

class addPayment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

class addOnlinePayment(forms.ModelForm):
    class Meta:
        model = OnlinePayment
        fields = "__all__"

class addContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"