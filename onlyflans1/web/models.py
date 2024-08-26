import uuid
from django.db import models


class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to="flans", null= True, blank= True)
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    customer_city = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Contact Form {self.customer_name} - {self.customer_email} - {self.customer_city}"

class Comunity(models.Model):
    comunity_uuid = models.UUIDField(default=uuid.uuid4, editable = True, unique = False)
    country = models.CharField(max_length=64)
    comunity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.comunity_name


