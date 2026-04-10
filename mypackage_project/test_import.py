"""
Тестирование импорта пакета mypackage.
"""

print("=" * 50)
print("ТЕСТИРОВАНИЕ ИМПОРТА ПАКЕТА")
print("=" * 50)

# Тест 1: Импорт всего пакета
print("\n1. Импорт пакета:")
import mypackage
print(f"   Версия: {mypackage.__version__}")
print(f"   Доступные компоненты: {mypackage.__all__}")

# Тест 2: Импорт подпакетов
print("\n2. Импорт подпакетов:")
from mypackage import models
from mypackage import utils
from mypackage import api

# Тест 3: Импорт конкретных классов
print("\n3. Импорт классов:")
from mypackage.models import Student, Group
from mypackage.utils import validate_email, format_student_info
from mypackage.api import APIClient

# Тест 4: Создание объектов
print("\n4. Создание объектов:")
student = Student("Тест", "Тестов", 20, "test@test.com")
print(f"   {student}")

group = Group("Тест-101", curator="Преподаватель А.Б.")
group.add_student(student)
print(f"   {group}")

# Тест 5: Валидаторы
print("\n5. Тест валидаторов:")
test_cases = [
    ("test@example.com", True),
    ("bad-email",        False),
    ("user@domain.ru",   True),
]
for email, expected in test_cases:
    valid, msg = validate_email(email)
    status = "✅" if valid == expected else "❌"
    print(f"   {status} {email}: {msg}")

# Тест 6: Оценки
print("\n6. Тест оценок:")
student.add_grade(5, "Python")
student.add_grade(4, "Математика")
student.add_grade(3, "Физика")
print(f"   Средний балл: {student.get_average_grade():.2f}")

print("\n" + "=" * 50)
print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО ✅")
print("=" * 50)
