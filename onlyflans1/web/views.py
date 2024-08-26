from django.shortcuts import render,redirect
from .models import Flan
from .forms import ContactFormModelForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST

def index(request):
    flanes = Flan.objects.all()
    public_flans = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flans': public_flans})
def mi_vista(request):
    flanes = Flan.objects.all()  # Obtén los objetos Flan desde tu modelo
    return render(request, 'index.html', {'flanes': flanes})
def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flans': private_flans})


def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data['customer_email']
            nombre = form.cleaned_data['customer_name']
            ciudad = form.cleaned_data['customer_city']
            return redirect('success', correo, nombre,ciudad)
    else:  # Si no hay parámetros de consulta
            form = ContactFormModelForm()
      # Creamos un formulario vacío para la solicitud GET
    return render(request, 'contacto.html', {'form': form})


def success(request, correo, nombre):
    return render(request, 'success.html', {'nombre': nombre, 'email': correo})


def login_view(request):
    return auth_vdefiews.LoginView.as_view()(request)

@require_POST
def logout_view(request):
    return auth_views.LogoutView.as_view()(request)

def comunity(request):

    return render(request,'comunity.html')