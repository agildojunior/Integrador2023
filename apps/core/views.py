from django.http.response import  HttpResponse
from django.shortcuts import render, redirect
from books.models.book import Book_Cart
from account.models.user import User
from account.models.adress import Adress
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator
from books.models import Book, Category
from books.models.cart import Cart
from transaction.models.transaction import Book_Transaction, Transaction
from django.db.models import Q


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
        Endereco = Adress.objects.create(user = user)
        Endereco.save()
        carrinho = Cart.objects.create(user = user)
        carrinho.save()

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
def inicioCategoria(request, nome): 
    cat = Category.objects.get(name=nome)
    livross = Book.objects.filter(category=cat.id).filter(~Q(quantity=0)).order_by('name')
    
    # --- paginação ---
    paginator1 = Paginator(livross, 12)
    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)

    context = {
        'livros': page_obj1,
    }
    return render(request, 'inicio/inicio.html', context)

# @login_required(login_url="/ifbook/login/")
def inicio(request): 
    livross = Book.objects.filter(~Q(quantity=0)).order_by('name')
    
    # --- paginação ---
    paginator1 = Paginator(livross, 12)
    page_number = request.GET.get('page')
    page_obj1 = paginator1.get_page(page_number)

    context = {
        'livros': page_obj1,
    }
    return render(request, 'inicio/inicio.html', context)

# @login_required(login_url="/ifbook/login/")
def carrinho(request):
    carrinhoUsuario = Cart.objects.get(user=request.user.id)
    carrinhoLivros = Book_Cart.objects.filter(cart=carrinhoUsuario)
    valor = 0
    for livro in carrinhoLivros:
        valor += float(livro.book.price)
    
    context = {
        'livroCarrinho': carrinhoLivros,
        'valor': valor,
    }
    return render(request, 'carrinho/carrinho.html', context)

# @login_required(login_url="/ifbook/login/")
def compras(request): 
    comprador = User.objects.get(id=request.user.id)
    transactionUsuario = Transaction.objects.filter(comprador=comprador)
    listaLivrostran = []
    for transactions in transactionUsuario:
        bookTransaction = Book_Transaction.objects.filter(transaction = transactions)
        for books in bookTransaction:
            listaLivrostran.append(books)
    import pdb
    livros = []
    for listaLivros in listaLivrostran:
        livrodalista = Book.objects.get(id=listaLivros.book.id)
        livros.append(livrodalista)
    context = {
        'livros': livros
    }
    return render(request, 'compras/compras.html', context)

# @login_required(login_url="/ifbook/login/")
def perfil(request): 
    user = request.user
    endereco = Adress.objects.filter(user=user.id).first()
    context = {
        'user':user,
        'endereco':endereco,
    }
    return render(request, 'perfil/perfil.html',context)

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

@login_required
def livrosEdit(request, id):
    livro = Book.objects.filter(id=id).first()
    category = Category.objects.all
    context = {
        'livro':livro,
        'category':category,
    }
    return render(request, 'book/editar_Livro.html',context)

@login_required
def livrosEdit2(request, id):
    # idcategoria = request.POST.get('categoria')
    # categoria = Categoria.objects.filter( id = idcategoria ).first()
    Book.objects.filter(id=id).update(
        name=request.POST.get('name'),
        quantity_pages=request.POST.get('quantity_pages'),
        note=request.POST.get('note'),
        year=request.POST.get('year'),
        price=request.POST.get('price'),
        quantity=request.POST.get('quantity'),
        synopsis=request.POST.get('synopsis'),
        status_book=request.POST.get('status_book'),
        publishing_company= request.POST.get('publishing_company'),
        category= request.POST.get('category'),
    )
    return redirect('livros')

@login_required
def add_book_in_cart(request, id_book):
    book = Book.objects.get(id=id_book)
    user = User.objects.get(id=request.user.id)
    cart = Cart.objects.get(user=user)
    
    cartBooks = Book_Cart.objects.filter(cart=cart)
    for livro in cartBooks:
        if livro.book.id == book.id:
            return redirect('carrinho')
     
    book_cart = Book_Cart.objects.create(book=book, cart=cart)   
    book_cart.save()
    
    return redirect('carrinho')


@login_required
def delete_book_in_cart(request, id_book):
    carrinho = Cart.objects.get(user=request.user.id)
    book = Book.objects.get(id=id_book)
    cartBook = Book_Cart.objects.filter(book=book, cart=carrinho).first()
    
    cartBook.delete()
    
    return redirect('carrinho')


@login_required
def infoLivro(request, id):
    book = Book.objects.get(id=id)
    context = {
        'livro':book,
    }
    return render(request, 'inicio/infoLivro.html',context)


def make_transaction(request):
    #pegar o usuario que está fazendo a transaction
    comprador = User.objects.get(id=request.user.id)
    #pegar o carrinho do usuario
    carrinhoUsuario = Cart.objects.get(user=comprador)
    #pega o livro do carrinho que o usuario quer comprar
    carrinhoLivros = Book_Cart.objects.filter(cart=carrinhoUsuario).all()
    
    for livrosCarrinho in carrinhoLivros:

        transaction = Transaction.objects.create(vendedor = livrosCarrinho.book.user, comprador=comprador)
        transactionBook = Book_Transaction.objects.create(transaction = transaction, book = livrosCarrinho.book)

        book = Book.objects.get(id=livrosCarrinho.book.id)
        book.quantity = int(book.quantity) - 1
        book.save()

        transaction.save()
        transactionBook.save()

        livrosCarrinho.delete()
        
    return redirect('compras')
        
@login_required
def userEdit(request):
    user = request.user
    username = request.POST.get('username')
    Adress.objects.filter(user=user.id).update(
        cep=request.POST.get('cep'),
        city=request.POST.get('city'),
        number=request.POST.get('number'),
        street=request.POST.get('street'),
        district=request.POST.get('district'),
    )
    # --- Verifica se o username ja existe ---
    username2 = User.objects.filter(username=username).first()
    if username != user.username:
        if username2:
            return HttpResponse('Esse usuario esta indisponivel')
    # ----------------------------------------
    User.objects.filter(id=user.id).update(
        username=request.POST.get('username'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone'),
    )

    return redirect('perfil')
        
        
        