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

