from faker import Faker

fake  = Faker(locale="fr_FR")
for i in range(10):
    print(fake.bothify(text="product number: ?%%%%%?"))