# from django.http import HttpResponse
from typing import Any
from django.shortcuts import render
from blog.data import posts
from django.http import HttpRequest

def blog(request):
    # Posso fazer o que eu quiser antes da resposta
    
    context = {
        # 'text': 'Olá blog',
        'title': 'titulo blog',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context 
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Exception('Post não existe.')
    
    context = {
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }

    return render(
        request,
        'blog/post.html',
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