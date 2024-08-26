from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('customer_email', 'customer_name', 'customer_city','message')
    customer_email = forms.EmailField(label = 'Correo')
    customer_name = forms.CharField(max_length=64, label = 'Nombre')
    customer_city = forms.CharField(max_length=100, label = 'Ciudad')
    message = forms.CharField(label = 'Mensaje')