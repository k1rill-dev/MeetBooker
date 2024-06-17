# Dockerfile для FastAPI приложения с использованием Poetry
FROM python:3.10-slim-buster

# Установим Poetry
RUN pip install poetry

# Установим рабочую директорию внутри контейнера
WORKDIR /app


# Скопируем только файлы Poetry
COPY ./pyproject.toml ./poetry.lock ./

# Установим зависимости
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Скопируем все файлы из проекта в контейнер
COPY . .

# Откроем порт для приложения
EXPOSE 8000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
