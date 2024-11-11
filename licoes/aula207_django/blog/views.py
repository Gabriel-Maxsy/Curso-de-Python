# from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    # Posso fazer o que eu quiser antes da resposta
    return render(
        request,
        'blog/index.html'
    )

def exemplo(request):
    # Posso fazer o que eu quiser antes da resposta
    return render(
        request,
        'blog/exemplo.html'
    )