from django.test import TestCase
from account.models import User

class UserTestModels(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_create_user(self):
        user = User.objects.create_user(
            username="everton",
            name="Everton Leite",
            email="everton@gmail.com",
            password="123",
            phone="84 99999-9999"    
        )
        user.save()
        self.assertEqual(user.username, "everton")
    
    def login_with_user(self):
        login = self.client.login(
            email= "everton@gmail.com",
            password= "123"
        )
        return login