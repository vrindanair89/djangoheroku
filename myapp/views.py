from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def testfunc1(request):
    return HttpResponse('hello world')
def testfunc2(request):
    return HttpResponse('<h1>Hiiii</h1>')
def testfunc3(request):
    return render(request,'index.html')
