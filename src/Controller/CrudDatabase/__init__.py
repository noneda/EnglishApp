from ...Model import db
from ...Model.Answers import Answer
from ...Model.Questions import Questions
from ...Model.Type import Type


class Crud():
    conn = db

    def __init__(self, *args, **kwargs) -> None:
        self.connect()
        self.create_tables()
        self.disconnect

    def create_tables(self):
        try:
            with self.conn:
                self.conn.create_tables([Type, Questions, Answer])
                self.conn.execute_sql('''
                    INSERT INTO Type (name, format)
                    VALUES ('OrdenBy', '{´Correct´ : '' , ´Words´ : [] }');
                ''')

                print("Tablas creadas exitosamente si no existian.")
        except self.conn.Error as e:
            print(f"Error al crear las tablas: {e}")

    def connect(self):
        try:
            self.conn = db
            self.conn.connect()
        except db.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def getData(self, id) -> dict:
        try:
            if not self.conn:
                self.connect()

            que = Questions.get(Questions.id == id)
            ans = Answer.get(Answer.question == que.id)

            send = {
                "Question" : (
                    que.id,
                    que.text,
                    que.Options,
                ),
                "Answer" : (
                    ans.id,
                    ans.accurate,
                )
            }

            return send
        except (Answer.DoesNotExist, Questions.DoesNotExist) as e:
            print(f"Error: No se encontró la pregunta o la respuesta con el ID {id}.")
            return None
        finally:
            self.disconnect()

    def getAllData(self) -> list:
        try:
            self.connect()

            all_data = []

            questions = Questions.select()
            for que in questions:
                ans = Answer.get_or_none(Answer.question == que.id)

                send = {
                    "Question" : (
                        que.id,
                        que.text,
                        que.Options,
                    ),
                    "Answer" : (
                        ans.id,
                        ans.accurate,
                    )
                }
                
                all_data.append(send)

            return all_data

        except db.Error as e:
            print(f"Error al obtener datos de preguntas y respuestas: {e}")
            return []

        finally:
            self.disconnect()

    def setData(self, id, queText, options, ansText) -> bool:
        try:
            self.connect()
            with self.conn.atomic():
                if id == None:
                    que = Questions.create(
                        type = 1, 
                        text=queText,
                        Options=options
                    )
                    ans = Answer.create(
                        type = 1, 
                        question=que.id,
                        accurate=ansText
                    )
                    print("Operación de creación exitosa!")
                    return True
                
                que = Questions.get_or_none(Questions.id == id)

                if que:
                    que.text = queText
                    que.Options = options
                    que.save()

                    ans = Answer.get(Answer.question == que.id)
                    ans.accurate = ansText
                    ans.save()

                    print("Operación de actualización exitosa!")
                else:
                    que = Questions.create(
                        type = 1, 
                        text=queText,
                        Options=options
                    )
                    ans = Answer.create(
                        type = 1, 
                        question=que.id,
                        accurate=ansText
                    )

                    print("Operación de creación exitosa!")

                return True

        except db.Error as e:
            print(f"Error al crear o actualizar pregunta y respuesta: {e}")
            return False

        finally:
            self.disconnect()

    def dropData(self, id) -> bool:
        try:
            self.connect()
            with self.conn.atomic():
                que = Questions.get(Questions.id == id)
                ans = Answer.get(Answer.question == que.id)
                ans.delete_instance()
                que.delete_instance()

            print("Operación de eliminación exitosa!")
            return True

        except (db.Error, Questions.DoesNotExist, Answer.DoesNotExist) as e:
            print(f"Error al eliminar pregunta y respuesta: {e}")
            return False

        finally:
            self.disconnect()
