# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Posso fazer o que eu quiser antes da resposta
    return render(
        request,
        'home/index.html'
    )