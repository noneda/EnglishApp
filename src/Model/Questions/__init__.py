from peewee import AutoField, TextField, ForeignKeyField  # type: ignore
from .. import base


from ..Type import Type

class Questions(base):
    id = AutoField()
    type = ForeignKeyField(Type, backref="types")

    text = TextField(null=False)
    Options = TextField(null=False)

