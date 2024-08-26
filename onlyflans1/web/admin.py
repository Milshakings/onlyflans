from django.contrib import admin
from .models import Flan
from .models import ContactForm

@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'slug', 'is_private')
    search_fields = ('name', 'description','image',)


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_city', 'message')
