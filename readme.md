# Streaming Microservice
## Обзор проекта
Это API является вторым из трех микросервисов, для ХИХИ-ХАХА сайта. 

Этот микросервис отвечает за отображения видео и данных о нем.

Этот API поддерживает:

- Отображение последних 50 видео.
- Отображение дополнительных 50 видео
- 
Остальные микросервисы:
- Микросервис отвечающий за регистрацию пользователей: https://github.com/ded2322/auth-microservice.git
- Микросервис отвечающий за загрузку видео: https://github.com/ded2322/upload-microservice.git
- Микросервис отвечающий за показ видео: [Текущий репозиторий]


## Инструменты

Язык: Python 3.10

Фреймворк: FastApi

База данных: Postgres 16


## Как запустить
1. С клонировать репозиторий
    ```text
    git clone https://github.com/ded2322/streaming-microservice.git
    ```

2. Перейти в директорию с файлом
    ```text
    cd streaming-microservice
    ```
3. Арендовать базу данных.
4. Создать .env файл и внести нужные данные в .env файл

    На основе [.env_exemple](.env_exemple) файла задать свои конфиги

5. Собрать и поднять docker-compose
    ```text
     docker-compose up --build 
    ```

### Обновления

v.1.0 

- Добавлен эндпоинт с отображением последних 50 видео
- Добавлен эндпоинт отвечающий за загрузку дополнительных 50 сообщений