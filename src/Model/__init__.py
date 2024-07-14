import os
from peewee import SqliteDatabase, Model # type: ignore

path =  os.getcwd() + "\\src\\Model\\Database\\English.db"

db = SqliteDatabase(path)

class base(Model):
    class Meta:
        database = db
