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

class FunctionalTestsAccount(TestCase, StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")
        self.superuser = User.objects.create_superuser(username='superuser', email='super@gmail.com', password='123')
        self.client.login(username='superuser', password='123')
        
    def test_page_register_user(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/cadastro/")    
        assert "Cadastro" in self.driver.title
    
    def test_page_login_user(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        assert "Login" in self.driver.title
        
    #funciona mas precisa mudar username sempre por estar salvando no banco de dados
    def test_register_user(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/cadastro/")
        time.sleep(2)
        assert "Cadastro" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("testando@gmail.com")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        assert "Login" in self.driver.title
        
    def test_register_user_existing(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/cadastro/")
        time.sleep(2)
        assert "Cadastro" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("testando@gmail.com")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        assert "" in self.driver.title
        
    def test_login_user(self):
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
        
        
        
    
