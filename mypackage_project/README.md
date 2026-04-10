# Лабораторная работа 9: Создание своего пакета и работа с внешними библиотеками

## Описание

Пакет `mypackage` для работы с данными о студентах и внешними REST API.

## Структура проекта

```
mypackage_project/
├── mypackage/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py      # Класс Student
│   │   └── group.py        # Класс Group
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py   # Функции валидации
│   │   └── formatters.py   # Функции форматирования
│   ├── api/
│   │   ├── __init__.py
│   │   └── client.py       # HTTP-клиент (requests)
│   └── data/
│       └── sample_data.json
├── main.py
├── test_import.py
├── requirements.txt
└── README.md
```

## Установка

```bash
# Создать и активировать виртуальное окружение
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Установить зависимости
pip install -r requirements.txt
```

## Запуск

```bash
# Запустить основную программу
python main.py

# Запустить тесты импорта
python test_import.py
```

## Возможности

- **Student** — создание студентов, добавление оценок, подсчёт среднего балла
- **Group** — управление группой студентов, поиск лучшего студента
- **Validators** — валидация email, возраста, оценок и имён
- **Formatters** — красивый вывод информации о студентах и группах
- **APIClient** — получение постов и пользователей с [JSONPlaceholder](https://jsonplaceholder.typicode.com), случайных цитат

## Пример использования

```python
from mypackage import Student, Group, APIClient, validate_email

# Создание студента
student = Student("Иван", "Петров", 19, "ivan@example.com")
student.add_grade(5, "Python")
student.add_grade(4, "Математика")
print(f"Средний балл: {student.get_average_grade():.2f}")

# Создание группы
group = Group("ПИН-231", curator="Иванова М.А.")
group.add_student(student)

# Работа с API
client = APIClient()
posts = client.get_posts(limit=3)
```
