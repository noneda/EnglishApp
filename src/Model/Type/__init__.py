from peewee import AutoField, CharField, TextField # type: ignore
from .. import base

class Type (base):
    id =  AutoField()

    name = CharField(
            max_length=50,
            null=True
        )
    
    format = TextField(null=True)
 