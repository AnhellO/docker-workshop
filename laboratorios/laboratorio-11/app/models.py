from peewee import Model, CharField, DateField
from db import db

class Question(Model):
    question_text = CharField()
    pub_date = DateField()

    class Meta:
        database = db

if db.table_exists('question') is False:
    db.create_tables([Question])