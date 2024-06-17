# Dockerfile для React приложения
FROM node:20.11.1-alpine

# Установим переменные окружения
ENV NODE_ENV=production

# Установим рабочую директорию внутри контейнера
WORKDIR /usr/src/app

# Скопируем package.json и установим зависимости
COPY ./package.json .

RUN npm install

# Скопируем все файлы из проекта в контейнер
COPY . .

# Откроем порт для приложения
EXPOSE 3000

# Команда для запуска приложения
CMD ["npm", "start"]
