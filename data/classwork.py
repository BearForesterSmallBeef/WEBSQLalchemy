import sqlalchemy
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
import datetime


SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory
    if __factory:
        return
    if not db_file or not db_file.strip():
        raise Exception("необходимо указать файл БД")
    conn_str = f'sqlite:///mars_explorer.db?check_same_thread=False'
    print(f'Подключение к БД: {conn_str}')

    engine = sqlalchemy.create_engine(conn_str, echo=False)
    # echo=True выводит сообщения в консоль, что дает удобную отладку
    __factory = orm.sessionmaker(bind=engine)
    # "noinspection PyUnresolvedReferences" не декларирует следущую строку
    # noinspection PyUnresolvedReferences
    from . import __all_models

    # создали все объекты базы данных
    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session: # явно указываем, что функция возвращает объект Session
    global __factory
    return __factory()


class Job(SqlAlchemyBase):
    __tablename__ = "jobs"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = sqlalchemy.Column(sqlalchemy.Integer)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    def __repr__(self):
        return f'<Job> {self.id}'
