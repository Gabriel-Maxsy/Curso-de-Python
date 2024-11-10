from django.http import HttpResponse
# from django.shortcuts import render

def blog(request):
    # Posso fazer o que eu quiser antes da resposta
    return HttpResponse('Blog do app')

def exemplo(request):
    # Posso fazer o que eu quiser antes da resposta
    return HttpResponse('exemplo do app')