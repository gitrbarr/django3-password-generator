from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    # return HttpResponse('Hello there friend!')
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def eggs(request):
    return HttpResponse('<h1>Eggs are awesome!</h1>')

def password(request):

    #characters = list('')
    #if request.GET.get('lowercase'):
    #    characters.extend(list('abcdefghijklmnopqrstuvwyxz'))
    characters = list('abcdefghijklmnopqrstuvwyxz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){}[]|,"~'))

    if len(characters) == 0:
        thepassword = 'You did not specify character types you fool'
    else:
        length = int(request.GET.get('length',12))
        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
