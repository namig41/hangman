# Виселица

"Виселица" - это классическая игра на угадывание слов, в которой игроки пытаются угадать скрытое слово, называя буквы по одной. За каждую неправильно угаданную букву игрок получает часть виселицы. Игра заканчивается, когда игрок угадывает слово или когда виселица полностью построена.

## Оглавление

- [Установка](#установка)
- [Правила игры](#правила-игры)
- [Использование](#использование)

## Установка

1. Склонируйте репозиторий на ваш локальный компьютер:
   ```bash
   git clone https://github.com/namig41/hangman.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd hangman
   ```

3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Правила игры

1. Игра выбирает случайное слово из списка.
2. Игрок должен угадывать буквы, которые могут быть в этом слове.
3. За каждую правильно угаданную букву, она отображается на своем месте в слове.
4. За каждую неправильно угаданную букву добавляется часть виселицы.
5. Игра заканчивается победой, если слово полностью угадано, или поражением, если виселица полностью построена.

## Использование

1. Запустите игру:
   ```bash
   python3 app/main.py
   ```

2. Следуйте инструкциям на экране, чтобы угадывать буквы.
