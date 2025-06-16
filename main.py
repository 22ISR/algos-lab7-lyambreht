"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

def isPalindrom(word):
    # оставляем только буквы и цифры
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    # сравниваем строку с её перевернутой версией
    return cleaned == cleaned[::-1]

# проверки
print(isPalindrom("level"))  # True
print(isPalindrom("hello"))  # False
print(isPalindrom("A man, a plan, a canal: Panama"))  # True


Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]


def isPalindrom(word):
    # оставляем только буквы и цифры
    cleaned = ''.join(c.lower() for c in word if c.isalnum())
    # сравниваем строку с её перевернутой версией
    return cleaned == cleaned[::-1]

# проверки
print(isPalindrom("level"))  # True
print(isPalindrom("hello"))  # False
print(isPalindrom("A man, a plan, a canal: Panama"))  # True

def isPalindromList(word_list):
    # берем list comprehension с вызовом isPalindrom из первого задания
    return [word for word in word_list if isPalindrom(word)]

# проверки
print(isPalindromList(["hello", "list", "level"]))  # ["level"]
print(isPalindromList(["Madam", "racecar", "python", "12321"]))  # ["Madam", "racecar", "12321"]


Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""

import re

def isPalindromString(text):
    # разбиваем текст на слова
    words = re.findall(r'\w+', text.lower())
    # находим уникальные палиндромы длиной больше 1 
    return sorted({word for word in words 
                 if word == word[::-1] and len(word) > 1})

# Тесты
print(isPalindromString("Madam, Anna went to the civic center"))  # ["anna", "civic", "madam"]
print(isPalindromString("Level, radar, test, noon"))  # ["level", "noon", "radar"]

