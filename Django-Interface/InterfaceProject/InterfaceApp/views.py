
from django.shortcuts import render, HttpResponse
from .models import Image
# Create your views here.
def index(request):
    Images = Image.objects.all()
    context = { 'Images': Images }
    return render(request, 'InterfaceApp/index.html', context)

def mondrian(request):
    return render(request, 'InterfaceApp/mondrian.html')

def gogh(request):
    return render(request, 'InterfaceApp/gogh.html')

def munch(request):
    return render(request, 'InterfaceApp/munch.html')




