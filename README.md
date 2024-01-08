# Таблица регистрации груза

### Описание проекта

Fullstack-приложение в формате SPA, построенное на Vue 3 и Django REST Framework (DRF). Представляет собой таблицу
регистрации груза с возможностью добавления, удаления и обновления данных в реальном времени. Backend реализован на
Django, а frontend использует Vue 3.

### Содержание

- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Функциональные возможности и описание](#функциональные-возможности-и-описание)

### Технологии

#### Frontend

- [Javascript](https://docs.celeryq.dev/en/stable/)
- [Vue](https://vuejs.org/): javascript-фреймворк для создания пользовательских интерфейсов.
- [Vuex PersistedState](https://www.npmjs.com/package/vuex-persistedstate): плагин для сохранения состояния Vuex в
  localStorage.
- [Vuex](https://vuex.vuejs.org/): состояние управления для Vue.js приложений.
- [Vite](https://vite-docs-ru.vercel.app/): сборщик (современная альтернатива webpack)  приложений на frontend`e.

#### Backend

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/): web-фреймворк для создания backend-части приложения.
- [PostgreSQL](https://www.postgresql.org/): реляционная база данных для хранения данных.
- [DRF](https://www.django-rest-framework.org/): расширение Django для создания API.

p.s объединяет `Docker`

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
  передаются на `backend`. После чего `frontend` обрабатывает их у себя и показывает и кэширует в сессионке (настройки
  сохраняются после обновления страницы).
* Таблица содержит фильтр и сортировку. Условия фильтра зависят от колонки по которой пользователь хочет произвести
  поиск. Сортировка включена в заголовки колонок, нажатия по которым будет её приводить в действие.
* Также присутствует пагинация на стороне сервера. `Frontend` же выводит количество страниц.
