from django.shortcuts import render
from .models import HairbraidingService

def hair_braiding(request):
    services = HairbraidingService.objects.all()
    return render(request, 'HairBraiding/hair_braiding.html', {'services'})

