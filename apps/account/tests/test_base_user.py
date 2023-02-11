from django.test import TestCase
from .factories import UserFactory
from account.models.user import User
from account.models.adress import Adress

class UserTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def create_user(self):
        user = User.objects.create_user(
            username="everton",
            name="Everton Leite",
            email="everton@gmail.com",
            password="123",
            phone="84 99999-9999"    
        )
        return user
    
    def create_adress(self):
        user = UserFactory()
        adress = Adress.objects.create(
            street = "Av. Independencia",
            number = "100",
            district = "Centro",
            cep = "59900-000",
            city = "Pau dos Ferros",
            state = "RN",
            complement = "ao lado do shopping",
            user = user
        )
        return adress
    