# src/models/quiz_model.py
from src.database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, PickleType


# INCOMPLETE: Define the QuizModel class
# TODO: Create a class named QuizModel that inherits from db.Model
class QuizModel(db.Model):
    # INCOMPLETE: Set up the table name
    # TODO: Define `__tablename__` as 'quizzes'
    __tablename__ = 'quizzes'

    # INCOMPLETE: Define table columns
    # TODO: Define an integer primary key column named `id`
    # TODO: Define a string column named `title` that cannot be null
    # TODO: Define a column named `questions` with PickleType to store a list
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    questions: Mapped[list] = mapped_column(PickleType, nullable=False)

    def __init__(self, title, questions):
        # INCOMPLETE: Initialize the model with title and questions
        # Assign `self.title` and `self.questions` with `title` and `questions`
        self.title = title
        self.questions = questions

    def save(self):
        # INCOMPLETE: Save the quiz to the database
        # Use `db.session.add(self)` and
        # `db.session.commit()` to save the instance
        db.session.add(self)
        db.commit()

    @classmethod
    def get_quiz(cls, quiz_id):
        # INCOMPLETE: Retrieve a quiz by its ID
        # Use `cls.query.get(quiz_id)` to retrieve a quiz and return it
        return cls.query.get(quiz_id)
