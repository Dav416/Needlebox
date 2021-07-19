from django.shortcuts import render

def myfirstview(request):

    return render(request, 'index.html')

# Create your views here.