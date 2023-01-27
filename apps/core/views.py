from django.http.response import  HttpResponse
from django.shortcuts import render, redirect
from apps.account.models.user import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.books.models import Book

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Esse usuario ja existe')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return render(request, 'login/login.html')

def logar(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'login/login.html')

# @login_required(login_url="/ifbook/login/")
def inicio(request): 
    livross = Book.objects.all()
    
    # --- paginação ---
    paginator1 = Paginator(livross, 12)
    page_number = request.GET.get('page')
    livros = paginator1.get_page(page_number)

    context = {
        'livros':livros,
    }
    return render(request, 'inicio/inicio.html',context)

# @login_required(login_url="/ifbook/login/")
def carrinho(request): 
    return render(request, 'carrinho/carrinho.html')

# @login_required(login_url="/ifbook/login/")
def compras(request): 
    return render(request, 'compras/compras.html')

# @login_required(login_url="/ifbook/login/")
def perfil(request): 
    return render(request, 'perfil/perfil.html')

# @login_required(login_url="/ifbook/login/")
def produtos(request): 
    return render(request, 'produtos/produtos.html')

# @login_required(login_url="/ifbook/login/")
def produtosAdd(request): 
    return render(request, 'adicionarLivro.html')

@login_required
def deslogar(request):
    logout(request)
    return redirect('inicio')
