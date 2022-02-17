import sqlalchemy as sa
from datetime import datetime
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "user"
    # primary_key указывает на то, что столбец будет ключем, а autoincrement создает id
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # nullable означает что строечка может ничего не содержать
    name = sa.Column(sa.Column, nullable=True)
    about = sa.Column(sa.Column, nullable=True)
    # unique проверка на уникальность поля, a index отвечает за то, чтобы быстрее найти эту информацию
    # он добавляет его в буфер, что делает добаление медленне, но поиск быстрее
    email = sa.Column(sa.Column, nullable=True, unique=True, index=True)
    name = sa.Column(sa.Column, nullable=True)

