# USER CRUD. ТАБЛИЦА С CRUD-ФУНКЦИЯМИ НАД ПОЛЬЗОВАТЕЛЯМИ

### Простое консольное приложение для управления пользователями с базой данных SQLite

---

1. Как установить?
   
Клонируйте репозиторий:

```bash
   git clone https://github.com/kaguguljyan/user-crud.git
   cd user-crud
```

Создайте виртуальное окружение:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

---

2. Как запустить?

2.1. Интерактивный режим

```bash
python -m src.users
```

2.2. С использованием аргументов (пример)

```bash
python -m src.cli add --name "имя" --age 25
```

---

# CLI-ИНСТРУКЦИЯ

Основные команды:

| Команда                  | Описание                          | Пример                          |
|--------------------------|-----------------------------------|---------------------------------|
| add --name NAME --age AGE | Добавить пользователя            | `add --name "Анна" --age 25`    |
| list                     | Показать всех пользователей      | `list`                          |
| update --id ID [--name] [--age] | Обновить данные               | `update --id 1 --name "Новое имя"` |
| delete --id ID            | Удалить пользователя             | `delete --id 2`                 |

Примеры:

1. Добавление пользователя:
   
```bash
python -m src.cli add --name "Ольга" --age 30
```

2. Показать всех пользователей:

```bash
python -m src.cli list
```

3. Обновление данных:

```bash
python -m src.cli update --id 1 --name "Николай"
```

4. Удаление пользователя:

```bash
python -m src.cli delete --id 1
```
