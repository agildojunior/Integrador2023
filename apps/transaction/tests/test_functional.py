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
        
    def test_page_minhas_compras(self):
        self.driver.get("http://127.0.0.1:8000/ifbook/login/")
        sleep(2)
        assert "Login" in self.driver.title

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys("testando")

        password = self.driver.find_element(By.NAME, "senha")
        password.send_keys("123")

        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
        
        self.driver.get("http://127.0.0.1:8000/ifbook/compras/")    
        assert "Minhas compras" in self.driver.title
    
    def test_transaction_book(self):
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
        
        sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/main/div/ul/li[2]/div/a").click()
        assert "Minhas compras" in self.driver.title
        
        
        
        
        
        