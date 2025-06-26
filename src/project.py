# импортируем нужные инструменты из библиотеки SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

engine = create_engine("sqlite:///users.db")  # подключаемся к бд SQLite
Base = declarative_base()  # создаём базовый класс для таблицы
Session = sessionmaker(bind=engine)  # создаём сессии


class User(Base):  # создаём класс Note, который представляет таблицу в бд
    __tablename__ = "users"  # указываем имя таблицы в бд
    id = Column(Integer, primary_key=True)  # id- главный ключ
    name = Column(String(50))  # name- строка
    age = Column(Integer)  # age- целое число
    created_at = Column(DateTime, default=datetime.now)  # created_at- дата добавления


Base.metadata.drop_all(engine) # удаляем таблицу users
Base.metadata.create_all(engine)  # создаём таблицу users


def load_users():  # загружаем все заметки из бд
    """Загружает заметки из файла."""
    session = Session()  # соединяемся с бд
    users = session.query(User).all()  # получаем всех пользователей из таблицы
    session.close()  # закрываем соединение
    return users  # возвращаем список пользователей


def add_user(name, age):  # добавляем пользователя
    """Добавляет новую заметку."""
    session = Session()
    user = User(
        name=name, age=age
    )  # создаём объект пользователя с переданным именем и возрастом
    session.add(user)
    session.commit()
    session.close()
    print("Пользователь добавлен")


def show_users():  # показываем всех пользователей
    """Показывает заметки."""
    session = Session()
    users = session.query(User).all()  # получаем всех пользователей из таблицы
    session.close()
    if not users: # если список пуст
        print("Пользователей нет")
        return
    print("Пользователи: ")
    for user in users:
        print(f"{user.id}, {user.name}")
        print(f"{user.age}")
        print(f"{user.created_at}")


def update_user(user_id, name=None, age=None): # обновляем данные пользователя
    session = Session()
    user = session.get(User, user_id) # находим пользователя по id
    if not user: # если пользователя с таким id нет
        print("Пользователя нет")
        session.close()
        return
    if name: # если передано новое имя
        user.name = name
    if age: # если передан новый возраст
        user.age = age
    session.commit()
    session.close()
    print("Обновлены данные пользователя")


def delete_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    if not user:
        print("Пользователя нет")
        session.close()
        return
    session.delete(user)
    session.commit()
    session.close()
    print("Пользователь удален")


def main():
    users = load_users()  # загружаем пользователей при запуске

    while True:
        print("База данных пользователей")
        print("1. Добавить пользователя в таблицу")
        print("2. Показать пользователей с таблицы")
        print("3. Обновить данные о пользователе в таблице")
        print("4. Удаленить пользователя из таблицы")
        print("5. Выход")

        choice = input("Выберите операцию: ")

        if choice == "1":
            name = input("Введите имя: ")
            age = int(input("Введите возраст: "))
            add_user(name, age)
            print("Пользователь добавлен!")
        elif choice == "2":
            show_users()
        elif choice == "3":
            user_id = int(input("Введите id пользователя для обновления: "))
            name = input("Введите имя: ")
            age_input = input("Введите возраст: ")
            if age_input: # обработка ввода возраста
                age = int(age_input)
            else:
                age = None
            if name: # обработка ввода имени
                new_name = name
            else:
                new_name = None
            update_user(user_id, new_name, age)
            print("Данные пользователя обновлены!")
        elif choice == "4":
            user_id = int(input("Введите id пользователя для удаления: "))
            delete_user(user_id)
        elif choice == "5":
            print("Вы вышли из программы")
            break
        else:
            print("Некорректный ввод")

if __name__ == "__main__":
    main()