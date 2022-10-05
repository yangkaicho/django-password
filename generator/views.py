from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def password(request):
    return render(request,'./password.html',{'password':123456})

def index(request):
    print('Hello Django')

    
    return render(request,'index.html',{'password':123456})