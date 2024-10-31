# api_final_yatube
Проект API для социальной сети Yatube.
Позволяет создавать, читать, изменять и удалять свои посты, а так же читать чужие посты и подписываться на их авторов посредством API-запросов.
Для неавторизованных пользователей API доступен только для чтения.
## Стек технологий:
Python 3.9.10, Django 3.2.16, DRF, JWT
## Как запустить проект:

Перед запуском необходимо склонировать проект:

```
git clone https://github.com/Oleg-Bagnii/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
