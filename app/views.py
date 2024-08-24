from django.shortcuts import render

def jinja_print(request):
    d={'name':'ashu','age':4}
    return render(request,'jinja_print.html',d)
# Create your views here.
