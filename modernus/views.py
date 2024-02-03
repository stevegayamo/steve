from django.shortcuts import render, redirect, get_object_or_404
from .models import Appliance, ApplianceImage
from .forms import ApplianceForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def appliances(request):
    appliances = Appliance.objects.all()
    return render(request, 'pages/appliances.html', {'appliances': appliances})

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def admin_appliances(request):
    appliances = Appliance.objects.all()
    return render(request, 'pages/admin/appliances.html', {'appliances': appliances})


def admin_appliances_add(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST, request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            appliance = form.save()    
            handle_image_uploads(request, appliance)
            return redirect('appliances_list')
    else:
        form = ApplianceForm()

    return render(request, 'pages/admin/add-appliances.html', {'form': form})


def admin_appliances_edit(request, appliance_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)

    if request.method == 'POST':
        form = ApplianceForm(request.POST, instance=appliance)
        if form.is_valid():
            appliance = form.save()
            handle_image_uploads(request, appliance)
            return redirect('appliances_edit', appliance_id=appliance.id)  
    else:
        form = ApplianceForm(instance=appliance)

    return render(request, 'pages/admin/edit-appliances.html', {'form': form, 'appliance': appliance})

def admin_appliances_delete(request, id):
    return render(request, 'pages/admin/appliances_delete.html')

def handle_image_uploads(request, appliance):
    for image_file in request.FILES.getlist('images'):
        ApplianceImage.objects.create(appliance=appliance, image=image_file)

def admin_appliances_delete(request, appliance_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    appliance.delete()
    return redirect('appliances_list')

def admin_appliances_image_delete(request, appliance_id, image_id):
    appliance = get_object_or_404(Appliance, pk=appliance_id)
    image = get_object_or_404(ApplianceImage, pk=image_id)
    image.delete()
    return redirect('appliances_edit', appliance_id=appliance.id) 