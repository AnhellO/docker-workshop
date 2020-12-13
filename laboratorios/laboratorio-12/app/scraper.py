import requests
from peewee import *
from faker import Faker
from models import MyCats

fake = Faker()

for _ in range(10):
    r = requests.get('https://aws.random.cat/meow')
    
    if r.status_code == 200 and 'file' in r.json():
        cat = MyCats(
            nombre=fake.unique.first_name(),
            imagen=r.json()['file']
        )
        
        print(f"##### Insertando registro...\n\t-> Registro: {cat}\n\t-> Status: {cat.save()}")
