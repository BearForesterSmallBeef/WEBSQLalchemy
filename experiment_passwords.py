from werkzeug.security import generate_password_hash, check_password_hash

password = input("Введите новый пароль?")
# Создаем хэш для пароля:
hashed_password = "pbkdf2:sha256:260000$8to3mH3HtIK5v5iu$14312cc99dd8c39f58172a5b3ba388e395b74a19fc2b12a8e056ed773c727b2b"
# Выводим хэш:
print(hashed_password)
bool_check = False
while not bool_check:
    check_password = input("Введите пароль:")
    # Проверяем пароль на правильность:
    bool_check = check_password_hash(hashed_password,
                                        check_password)
    # Сообщаем пользователю результат и заодно отслеживаем хэш:
    if bool_check:
        print("Пароль верный! У него хэш:")
    else:
        print("Неверный пароль! У него хэш:")
    print(generate_password_hash(check_password))
