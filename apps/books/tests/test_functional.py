import os
import time
from time import sleep
from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from account.models.user import User
from utils.browser import make_chrome_browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTestsBooks(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.superuser = User.objects.create_superuser(username='superuser', email='super@gmail.com', password='123')
        self.client.login(username='testando', password='123')
        
    def test_page_livros(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        self.driver.get("http://127.0.0.1:8000/ifbook/livros/")    
        assert "Meus Livros" in self.driver.title
    
    def test_page_add_book(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        self.driver.get("http://127.0.0.1:8000/ifbook/livros/adicionar")
        assert "Adicionar Livro" in self.driver.title
    
    def test_add_book(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        time.sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        self.driver.get("http://127.0.0.1:8000/ifbook/livros/adicionar")
        assert "Adicionar Livro" in self.driver.title
        
        name = self.driver.find_element(By.NAME, "name")
        name.send_keys("Livro Teste")
        sleep(2)
        book_cover = self.driver.find_element(By.NAME, "book_cover")
        book_cover.send_keys(
            os.getcwd() + "\images\capa.jpeg"
        )
        sleep(2)
        quantity_pages = self.driver.find_element(By.NAME, "quantity_pages")
        quantity_pages.send_keys("100")
        
        self.driver.find_element(By.ID, "id_status_book").click()
        
        self.driver.find_element(By.XPATH, "/html/body/main/form/div[2]/div[1]/div/select/option[3]").click()
        
        status_book = self.driver.find_element(By.NAME, "status_book")
        status_book.send_keys("Novo")
        
        author = self.driver.find_element(By.NAME, "author")
        author.send_keys("Clarisse Lispector")
        
        note = self.driver.find_element(By.NAME, "note")
        note.send_keys("Arranhão na capa")
        
        year = self.driver.find_element(By.NAME, "year")
        year.send_keys("testando")
        
        price = self.driver.find_element(By.NAME, "price")
        price.send_keys("testando")
        
        quantity = self.driver.find_element(By.NAME, "quantity")
        quantity.send_keys("testando")
        
        synopsis = self.driver.find_element(By.NAME, "synopsis")
        synopsis.send_keys("testando")
        
        publishing_company = self.driver.find_element(By.NAME, "publishing_company")
        publishing_company.send_keys("testando")
        
        self.driver.find_element(By.ID, "id_category").click()
        sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/main/form/div[2]/div[9]/div/select/option[9]").click()
        sleep(2)
        button = self.driver.find_element(By.CLASS_NAME, "btn")
        button.send_keys(Keys.RETURN)
        self.driver.get("http://127.0.0.1:8000/ifbook/livros/")    
        assert "Meus Livros" in self.driver.title
    
    def test_delete_book(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        time.sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        self.driver.get("http://127.0.0.1:8000/ifbook/livros/")
        assert "Meus Livros" in self.driver.title
        
        self.driver.find_element(By.XPATH, "/html/body/form/div/table/tbody/tr/td[8]/a[1]").click()
        
        assert "Apagar Livro" in self.driver.title
        
        self.driver.find_element(By.XPATH, "/html/body/main/form/section/div[2]/p/input").click()
        
        assert "Meus Livros" in self.driver.title
        
    def test_add_book_in_cart(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        time.sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        assert "Inicio" in self.driver.title
       
        
        self.driver.find_element(By.CLASS_NAME, "btn-group")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/div[1]/div[1]/div/div/h6/div/div").click()
        
        assert "Carrinho" in self.driver.title
        
        
        
        