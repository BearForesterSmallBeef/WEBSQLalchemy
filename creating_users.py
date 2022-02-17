from flask import Flask
from data import db_session
from data.users import User


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    # for i in range(1, 4):
    #     user = User()
    #     user.name = f"Пользователь {i}"
    #     user.about = f"Биография пользователя {1}"
    #     user.email = f"email{i}@email.ru"
    #     db_sess = db_session.create_session()
    #     db_sess.add(user)
    #     db_sess.commit()

    # получение данных
    user = db_sess.query(User).first()
    print(user)


if __name__ == "__main__":
    main()
