from account.tests import test_base_user
from account.tests.factories import UserFactory, AdressFactory

class UserTestModels(test_base_user.UserTestModels):
    def setUp(self):
        self.user = self.create_user()
        self.adress = self.create_adress()

    #USER
    def test_user_str(self):
        user = UserFactory()
        print(user)
        self.assertEqual(str(user), user.username)

    def test_user_username(self):
        self.assertIsNotNone(self.user.username)
        
    def test_user_name(self):
        self.assertIsNotNone(self.user.name)
                
    def test_user_email(self):
        self.assertIsNotNone(self.user.email)
    
    def test_user_password(self):
        self.assertTrue(self.user.check_password("123"))
        self.assertIsNotNone(self.user.check_password("123"))
        self.assertFalse(self.user.check_password("wrong_password"))
        
    def test_user_phone(self):
        self.assertEqual(self.user.phone, "84 99999-9999")
        
    
    #ADRESS
    def test_adress_str(self):
        adress = AdressFactory()
        print(adress)
        self.assertEqual(str(adress), adress.city)
    
    def test_adress_street(self):
        self.assertIsNotNone(self.adress.street)
        
    def test_adress_number(self):
        self.assertIsNotNone(self.adress.number)
        
    def test_adress_district(self):
        self.assertIsNotNone(self.adress.district)
        
    def test_adress_cep(self):
        self.assertIsNotNone(self.adress.cep)
    
    def test_adress_city(self):
        self.assertIsNotNone(self.adress.city)
        
    def test_adress_complement(self):
        self.assertIsNotNone(self.adress.complement)