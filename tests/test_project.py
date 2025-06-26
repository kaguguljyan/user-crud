import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.project import add_user, show_users, update_user, delete_user, load_users


class TestUser(unittest.TestCase):

    # очищаем базу данных перед каждым тестом
    def setUp(self):
        all_users = load_users()
        for user in all_users:
            delete_user(user.id)

    # тест добавления пользователя
    def test_add_user(self):
        add_user("Лера", 25)  # добавляем пользователя
        users = load_users()  # загружаем всех пользователей

        # проверка на добавления пользователя
        self.assertEqual(len(users), 1)  # должен быть 1 пользователь
        self.assertEqual(users[0].name, "Лера")  # имя должно быть "Анна"
        self.assertEqual(users[0].age, 25)  # возраст должен быть 25

    # тест показа всех пользователей
    def test_show_users(self):
        add_user("Ксения", 22)  # добавляем пользователя

        # вызываем функцию. Если не будет ошибок, тест пройдёт
        show_users()  # выводим всех пользователей

    # тест обновления пользователя
    def test_update_user(self):
        add_user("Алиса", 16)  # добавляем пользователя
        user_id = load_users()[0].id  # получаем его ID

        update_user(user_id, "Алиса", 25)  # обновляем данные
        updated_user = load_users()[0]  # загружаем обновлённого пользователя

        # проверка изменения
        self.assertEqual(updated_user.name, "Алиса")
        self.assertEqual(updated_user.age, 25)

    # тест удаления пользователя
    def test_delete_user(self):
        add_user("Светлана", 45)  # добавляем пользователя
        user_id = load_users()[0].id  # получаем его ID

        delete_user(user_id)  # удаляем пользователя
        users = load_users()  # загружаем всех пользователей

        # проверка на пустой список
        self.assertEqual(len(users), 0)


if __name__ == "__main__":
    unittest.main()