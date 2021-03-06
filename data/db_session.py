import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec


SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file):
    global __factory
    if __factory:
        return
    if not db_file or not db_file.strip():
        raise Exception("необходимо указать файл БД")
    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f'Подключение к БД: {conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
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
