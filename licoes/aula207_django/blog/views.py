# from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    # Posso fazer o que eu quiser antes da resposta
    
    context = {
        'text': 'Olá blog',
        'title': 'titulo blog'
    }
    return render(
        request,
        'blog/index.html',
        context 
    )

def exemplo(request):
    # Posso fazer o que eu quiser antes da resposta
    context = {
        'text': 'Olá exemplo',
        'title': 'Pagina de exemplo'
    }
    return render(
        request,
        'blog/exemplo.html',
        context
    )