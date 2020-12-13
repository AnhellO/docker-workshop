from peewee import *
from faker import Faker

# Para generar valores random en los rows
fake = Faker()

# Crea conexión con la DB
db = PostgresqlDatabase(
    'random_cats',
    user='the_cat',
    password='secretcat123',
    host='localhost',
    port=5432
)

# ORM con una tabla
class MyCats(Model):
	nombre = CharField()
	imagen = CharField()

	class Meta:
		database = db
		table_name = 'my_cats'

	def __str__(self):
		return f"ID: {self.id}\nNombre: {self.nombre}\nImagen: {self.imagen}"

# Conectate a la DB
db.connect()
print("¡Conectado!")

# Creamos un registro
some_cat = MyCats.create(nombre=fake.unique.first_name(), imagen=fake.url())
print("Inserté un nuevo registro:")
print(some_cat)

# Obtén solo un registro
some_other_cat = MyCats.get()
print("Busqué un registro:")
print(some_other_cat)

# Actualizamos algunos registros
some_cat.name = fake.unique.first_name()
some_other_cat.name = fake.unique.first_name()
some_other_cat.imagen = fake.url()
some_cat.save()
some_other_cat.save()
print("Actualicé mis registros:")
print(some_cat)
print(some_other_cat)

# Añade un nuevo registro si es que no existe
charizardo = MyCats.get_or_create(nombre='Charizardo', imagen='https://purr.objects-us-east-1.dream.io/i/G4Iu1.jpg')
print("Inserté un nuevo registro:")
print(charizardo)

# Obtén múltiples registros
print("Busco múltiples registros:")
cats = MyCats.select()
for _cat in cats:
	print(_cat)

listita = [_cat.nombre for _cat in cats]
print(listita)

# Borra algunos registros
print("Borro algunos registros:")
print(MyCats.delete().where(MyCats.id == MyCats.get().id).execute())
# print(some_cat.delete_instance())

# *SIEMPRE* recuerda cerrar la conexión
db.close()