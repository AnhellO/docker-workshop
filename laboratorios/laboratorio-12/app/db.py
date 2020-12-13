import settings
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    settings.DATABASE['NAME'],
    user=settings.DATABASE['USER'],
    password=settings.DATABASE['PASSWORD'],
    host=settings.DATABASE['HOST'],
)
