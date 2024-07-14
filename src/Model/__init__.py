from peewee import SqliteDatabase, Model # type: ignore

db = SqliteDatabase(".\Model\Database\English.db")

class base(Model):
    class Meta:
        database = db
