# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # Posso fazer o que eu quiser antes da resposta
    context = {
        'text': 'pagina home',
        'title': 'titulo da home'
    }
    return render(
        request,
        'home/index.html',
        context
    )