from peewee import Model, CharField
from db import db

class MyCats(Model):
	nombre = CharField()
	apellido = CharField()
	imagen = CharField()

	class Meta:
		database = db
		table_name = 'my_cats'

	def __str__(self):
		return f"ID: {self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Imagen: {self.imagen}"