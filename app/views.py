from django.shortcuts import render

# Create your views here.
def fun1(request):
    return render(request,'one.html')
def fun2(request):
    return render(request,'rwo.html')
