from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from account.models.user import User
from account.models.adress import Adress

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    name = Faker("name")
    username = Faker("user_name")
    email = Faker("email")
    password = Faker("password", length=6)
    phone = Faker("phone_number")


class AdressFactory(DjangoModelFactory):
    class Meta:
        model= Adress
        
    street = Faker("street_name")
    number = Faker("building_number")
    district = Faker("street_suffix")
    cep = Faker("postcode")
    city = Faker("city")
    state = Faker("random_element", elements=(
            "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO",
            "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI",
            "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"
        ))
    complement = Faker("secondary_address")
    user = SubFactory(UserFactory)