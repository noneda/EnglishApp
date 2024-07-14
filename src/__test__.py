from Model import db

from Model.Type import Type
from Model.Questions import Questions
from Model.Answers import Answer

db.connect()
db.create_tables(
    [
        Type,
        Questions,
        Answer
    ]
)

db.close()

