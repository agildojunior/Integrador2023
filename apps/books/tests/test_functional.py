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
        time.sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        self.driver.get("http://127.0.0.1:8000/ifbook/livros/")    
        assert "Meus Produtos" in self.driver.title
    
    def test_page_add_book(self):
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
        