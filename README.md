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

#### Дополнительно

- [Docker](https://www.docker.com/): приложение для контениризации.
- [Unittest](https://docs.python.org/3/library/unittest.html): модуль тестирования (в данном случае используется
  специальный
  пакет rest_framework.test).

### Начало работы

**Запустить проект можно воспользовавшись только запуском Docker контейнера, остальное - по желанию.**

#### Docker

*Необходимо иметь на компьютере Docker и Docker-compose*

После клонирования проекта запустите его в терминале с помощью команды:

```sh
$ docker-compose up --build
```

---

#### Backend

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

### URL `эндпоинты`:

_Backend_

* `http://0.0.0.0:8000/shipments/` - основной путь для получения отгрузок
* `http://0.0.0.0:8000/shipments/create/` - путь создания отгрузки
* `http://0.0.0.0:8000/shipments/delete/<int:pk>/` - путь удаления отгрузки
* `http://0.0.0.0:8000/shipments/update/<int:pk>/` - путь обновления отгрузки

---
_Frontend_

* `http://localhost:5173/` - отображает фронтенд (главную страницу)

### Функциональные возможности и описание

* Таблица состоит из: _даты, времени, маркировки, документа, поставщика, счетовода, водителя,_ а также: _заявленному,
  принятому и оставшемуся по количеству грузу._
* Присутствует возможность добавление, удаления и и обновления данных в таблицы в реальном времени. Эти данные
  передаются на `backend`. После чего `frontend` обрабатывает их у себя и показывает и кэширует в сессионке (настройки
  сохраняются после обновления страницы).
* Таблица содержит фильтр и сортировку. Условия фильтра зависят от колонки по которой пользователь хочет произвести
  поиск. Сортировка включена в заголовки колонок, нажатия по которым будет её приводить в действие.
* Также присутствует пагинация на стороне сервера. `Frontend` же выводит количество страниц.