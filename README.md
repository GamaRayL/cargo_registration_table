# Таблица регистрации груза

Приложение в формате `SPA`.
В данный `Fullstack` проект построен на `Vue_3` и `DRF (Django)`.

### Содержание

- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Функциональные возможности и описание](#функциональные-возможности-и-описание)

### Технологии

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [DRF](https://www.django-rest-framework.org/)
- [Javascript](https://docs.celeryq.dev/en/stable/)
- [Vue](https://vuejs.org/)
- [Vuex](https://vuex.vuejs.org/)

### Начало работы

#### Backend

После клонирования проекта, рекомендуется:

Установить виртуальное окружение:

```sh
$ python3 -m vevn venv
```

Установить список зависимостей:

```sh
$ pip install -r requirements.txt
```

Отредактировать .env файл под себя:

```python
# Debug
DEBUG = True
...
```

Зависимости:

```python
django
djangorestframework
psycopg2 - binary
django - cors - headers
django - filter
python - dotenv
coverage
pillow
```

#### Frontend

Установить список зависимостей:

```sh
$ npm install
```

Зависимости:

```vue
axios
vue
vue-router
vuex
vuex-persistedstate
devDependencies
@vitejs/plugin-vue
sass
vite
```

### Функциональные возможности и описание

* Таблица состоит из: _даты, времени, маркировки, документа, поставщика, счетовода, водителя,_ а также: _заявленому,
  принятому и оставшемуся по количеству грузу._
* Присутствует возможность добавление, удаления и и обновления данных в таблицы в реальном времени. Эти данные
  передаются на `backend`. После чего `frontend` обрабатывает их у себя и показывает.
* Таблица содержит фильтр и сортировку. Условия фильтра зависят от колонки по которой пользователь хочет произвести
  поиск. Сортировка включена в заголовки колонок, нажатия по которым будет её приводить в действие.
* Также присутствует пагинация на стороне сервера. `Frontend` же выводит количество страниц.
