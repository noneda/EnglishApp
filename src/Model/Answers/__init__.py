from peewee import AutoField, TextField , ForeignKeyField  # type: ignore
from .. import base


from ..Type import Type
from ..Questions import Questions

class Answer(base):
    id  = AutoField()
    type = ForeignKeyField(Type, backref="types")

    question = ForeignKeyField(Questions, backref="questions")    
    accurate = TextField(null = False) 