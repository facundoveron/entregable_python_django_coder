from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'posts/inicio.html')

def acerca_de(request):
    return render(request,'posts/acerca.html')