from django.test import Client, TestCase
from account.models.adress import Adress
from account.models.user import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import logout

from account.tests.factories import UserFactory
from books.models.book import Book, Book_Cart
from books.models.cart import Cart
from books.models.category import Category
from books.tests.test_base_books import BookFactory, CategoryFactory
from core.views import inicio
from transaction.models.transaction import Book_Transaction, Transaction

class CadastroTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Criar um usuário de teste para usar nos testes
        self.user = UserFactory()
        self.user2 = UserFactory()
        self.livro = BookFactory()
        self.livro2 = BookFactory()
        self.categoria = Category.objects.create(name="romance")
        image = SimpleUploadedFile("/images/capa.jpeg", b"file_content", content_type="image/jpeg")
        self.book = Book.objects.create(
            name = "Livro Teste 1",
            quantity_pages = "100",
            status_book = "Usado",
            book_cover = image,
            author = "Autor Teste",
            note = "Nota teste",
            year = "2000",
            price = "10",
            quantity = "2",
            synopsis = "Teste Sinopsis",
            publishing_company = "Teste Editora",
            category = self.categoria,
            user = self.user2
        )
        image2 = SimpleUploadedFile("/images/capa.jpeg", b"file_content", content_type="image/jpeg")
        self.book2 = Book.objects.create(
            name = "Livro Teste 2",
            quantity_pages = "100",
            status_book = "Usado",
            book_cover = image2,
            author = "Autor Teste",
            note = "Nota teste",
            year = "2000",
            price = "15",
            quantity = "2",
            synopsis = "Teste Sinopsis",
            publishing_company = "Teste Editora",
            category = self.categoria,
            user = self.user2
        )
        self.superuser = User.objects.create_superuser(username='superuser', email='super@gmail.com', password='123')
        self.cart = Cart.objects.create(user=self.superuser)
        self.book_cart_1 = Book_Cart.objects.create(cart=self.cart, book=self.book)
        self.book_cart_2 = Book_Cart.objects.create(cart=self.cart, book=self.book2)
        
        self.adress = Adress.objects.create(
            street="rua teste",
            number="numero teste",
            district="bairro teste",
            cep="teste cep",
            city="teste cidade",
            state="RN",
            complement="complemento teste",
            user=self.superuser
        )
        

    def test_login_with_valid_credentials(self):
        response = self.client.post('/ifbook/login/', {'username': self.user.username, 'password': self.user.password})
        self.assertEqual(response.status_code, 200)

    def test_login_with_invalid_credentials(self):
        response = self.client.post('/ifbook/login/', {'username': self.user.username, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)

    def test_login_with_get_request(self):
        response = self.client.get('/ifbook/login/')
        self.assertEqual(response.status_code, 200)

    def test_cadastro_user_sucess(self):
        response = self.client.get('/ifbook/cadastro/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/ifbook/cadastro/', {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword'
        }) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 6)

    def test_cadastro_user_fail(self):
        User.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword'
        )
        response = self.client.get('/ifbook/cadastro/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/ifbook/cadastro/', {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'senha': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Esse usuário já existe')
        self.assertEqual(User.objects.count(), 6)
    
    #FALTA TESTAR COMPLETAMENTE    
    def test_page_initial_categoria(self):
        response1 = self.client.post('/ifbook/login/', {'username': self.user.username, 'password': self.user.password})
        self.assertEqual(response1.status_code, 200)
        print(self.categoria)
        response = self.client.post('/ifbook/inicio/', {'nome': ''})
        self.assertEqual(response.status_code, 302)
 
    def test_inicio_template(self):
        self.client.login(username='superuser', password='123')
        response = self.client.post('/ifbook/inicio/', {'pesquisa': ''})
        print(response)
        self.assertTemplateUsed(response,'inicio/inicio.html')

    def test_inicio_with_search_term(self):
        self.client.login(username='superuser', password='123')
        response = self.client.post('/ifbook/inicio/', {'pesquisa': 'romance'})
        livros = Book.objects.filter(~Q(quantity=0)).filter(name='romance').order_by('name')
        paginator = Paginator(livros, 12)
        page_obj = paginator.get_page(1)
        self.assertEqual(str(response.context['livros']), str(page_obj))

    def test_inicio_without_search_term(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get('/ifbook/inicio/')
        livros = Book.objects.filter(~Q(quantity=0)).order_by('name')
        paginator = Paginator(livros, 12)
        page_obj = paginator.get_page(1)
        self.assertEqual(str(response.context['livros']), str(page_obj))
        
     #carrinho
    def test_carrinho_view(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get('/ifbook/carrinho/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'carrinho/carrinho.html')
    
    def test_carrinho_context(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get('/ifbook/carrinho/')
        livro_carrinho = Book_Cart.objects.filter(cart=self.cart)
        self.assertEqual(str(response.context['livroCarrinho']),str(livro_carrinho))
        valor = 0
        for livro in livro_carrinho:
            valor += float(livro.book.price)
        self.assertEqual(response.context['valor'], valor)
    
    def test_carrinho_sem_livros(self):
        user = User.objects.create_user(username='emptycart', password='123')
        cart = Cart.objects.create(user=user)
        self.client.login(username='emptycart', password='123')
        response = self.client.get('/ifbook/carrinho/')
        self.assertEqual(str(response.context['livroCarrinho']), '<QuerySet []>')
        self.assertEqual(response.context['valor'], 0)
    
    def test_compras_view_with_purchases(self):
        self.client.login(username='superuser', password='123')
        
        transaction = Transaction.objects.create(comprador=self.superuser, vendedor=self.book.user)
        Book_Transaction.objects.create(transaction=transaction, book=self.book)
        Book_Transaction.objects.create(transaction=transaction, book=self.book2)
        
        response = self.client.get('/ifbook/compras/')
        livros = response.context['livros']
        self.assertEqual(len(livros), 2)
        self.assertIn(self.book, livros)
        self.assertIn(self.book2, livros)
        
    def test_compras_view_without_purchases(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get('/ifbook/compras/')
        # livros = response.context['livros']
        # self.assertEqual(len(livros), 0)
        # # self.asserTrue(livros.is_empty())
        self.assertEqual(response.context['livros'], [])
    
    def test_user_perfil(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get('/ifbook/perfil/') 
        self.assertEqual(response.status_code, 200)
    
    def test_user_perfil_adress(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get('/ifbook/perfil/') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'superuser')
        self.assertContains(response, 'super@gmail.com')
        self.assertContains(response, 'rua teste')
        self.assertContains(response, 'numero teste')
        self.assertContains(response, 'teste cep')
        self.assertContains(response, 'teste cidade')
        self.assertContains(response, 'RN')
        
    def test_logout(self):
        self.client.login(username='superuser', password='123')
        self.client.get('/ifbook/deslogar/')
        self.client.logout()
        
        response = self.client.get('/ifbook/perfil/') 
        self.assertEqual(response.status_code, 302)

    def test_add_book_in_cart_success(self):
        self.client.login(username='superuser', password='123')
        response = self.client.get(f'/ifbook/carrinho/{self.book.id}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/ifbook/carrinho/')
        self.assertEqual(Book_Cart.objects.count(), 2)
        book_cart = Book_Cart.objects.first()
        self.assertEqual(book_cart.book, self.book)
        self.assertEqual(book_cart.cart, self.cart)
    
    def test_add_book_in_cart_fail(self):
        self.client.login(username='superuser', password='123')
        Book_Cart.objects.create(book=self.book, cart=self.cart)
        response = self.client.get(f'/ifbook/carrinho/{self.book.id}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/ifbook/carrinho/')
        self.assertEqual(Book_Cart.objects.count(), 3)
    
    def test_add_book_in_cart_not_authenticated(self):
        response = self.client.get(f'/ifbook/carrinho/{self.book.id}')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/ifbook/login/?next=/ifbook/carrinho/3')
        self.assertEqual(Book_Cart.objects.count(), 2)
        
    def test_delete_book_in_cart(self):
        self.client.login(username='superuser', password='123')
        self.assertEqual(Book_Cart.objects.filter(book=self.book2, cart=self.cart).count(), 1)

        # chamar a função delete_book_in_cart
        response = self.client.post('/ifbook/carrinho/excluir/' + str(self.book2.id))
        # verificar se o livro foi removido do carrinho
        self.assertEqual(Book_Cart.objects.filter(book=self.book2, cart=self.cart).count(), 0)

        # verificar se o redirecionamento para a página "carrinho" ocorreu corretamente
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/ifbook/carrinho/')
    
    def test_make_transaction(self):
        self.client.login(username='superuser', password='123')

        # verificar se o livro está no carrinho do comprador
        self.assertEqual(Book_Cart.objects.filter(book=self.book2, cart=self.cart).count(), 1)
        self.assertEqual(self.book2.quantity, str(2))

        # chamar a função make_transaction
        response = self.client.post('/ifbook/carrinho/comprar/')

        # verificar se o livro foi removido do carrinho do comprador
        self.assertEqual(Book_Cart.objects.filter(book=self.book2, cart=self.cart).count(), 0)

        # verificar se a quantidade do livro foi atualizada corretamente
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.quantity, str(1))

        # verificar se a transação foi criada corretamente
        self.assertEqual(Transaction.objects.filter(comprador=self.superuser).count(), 2)
        transaction = Transaction.objects.filter(comprador=self.superuser).first()
        self.assertEqual(transaction.vendedor, self.user2)

        # verificar se o livro foi adicionado à transação corretamente
        self.assertEqual(Book_Transaction.objects.filter(transaction=transaction).count(), 1)
        transaction_book = Book_Transaction.objects.get(book=self.book2)
        print(transaction_book.book)
        self.assertEqual(transaction_book.book, self.book2)

        # verificar se o redirecionamento para a página "compras" ocorreu corretamente
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/ifbook/compras/')
    