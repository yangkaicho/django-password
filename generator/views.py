from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
def password(request):
    chars=[chr(c) for c in range(97,123)]
    #print(chars)
    if request.GET.get('uppercase'):
        chars+=[chr(c).upper() for c in range(97,123)]
    if request.GET.get('number'):
        for i in range(10):
            chars+=str(i)
    print(chars)
    if request.GET.get('special'):
        chars+=list('@#$%^&*')
    lenght=eval(request.GET.get('lenght')) if request.GET.get('input-lenght')=='' else eval(request.GET.get('input-lenght'))

    password=''.join([random.choice(chars) for i in range(lenght)])
    print(password)
   
    
    
    return render(request,'./password.html',{'password':password})

def index(request):
    print('Hello Django')

    
    return render(request,'index.html',{'password':123456})