import sqlalchemy as sa
from datetime import datetime
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = "users"
    # primary_key указывает на то, что столбец будет ключем, а autoincrement создает id
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    # nullable означает что строечка может ничего не содержать
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    # unique проверка на уникальность поля, a index отвечает за то, чтобы быстрее найти эту информацию
    # он добавляет его в буфер, что делает добаление медленне, но поиск быстрее
    email = sa.Column(sa.String, nullable=True, unique=True, index=True)
    heshed_password = sa.Column(sa.String, nullable=True)
    # default значение по умолчанию
    create_date = sa.Column(sa.DateTime, default=datetime.now)
    news = orm.relation("News", back_populates="user")
