from django.shortcuts import render
from main.models import Writers

def bio_home(request):
    persons = Writers.objects.order_by('name')
    return render(request, 'bio/bio_home.html', {'persons':persons})

def bio_pushkin(request):
    return render(request, 'bio/bio_pushkin.html')

def bio_akhmatova(request):
    return render(request, 'bio/bio_akhmatova.html')

def bio_dostoevsky(request):
    return render(request, 'bio/bio_dostoevsky.html')

def bio_esenin(request):
    return render(request, 'bio/bio_esenin.html')

def bio_gorky(request):
    return render(request, 'bio/bio_gorky.html')

def bio_lermontov(request):
    return render(request, 'bio/bio_lermontov.html')

def bio_mayakovsky(request):
    return render(request, 'bio/bio_mayakovsky.html')

def bio_tsvetaeva(request):
    return render(request, 'bio/bio_tsvetaeva.html')