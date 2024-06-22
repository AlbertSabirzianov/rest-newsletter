# rest-newsletter
Броккер сообщений для rest сервисов - каждый участник может создавать 
новую тему (subject) сообщений, подписываться на любую существующую тему
с указанием url (адреса отправки сообщения) и отправлять сообщения по определённой теме.
При этом отправленное сообщение будет посланно всем подписавшимся на данную тему по
http на указанный url с помощью POST запроса. Пример сообщения
```json
{
  "subject_name": "string",
  "data": {}
}
```
# Как запустить
клонируйте репозиторий
```commandline
git clone https://github.com/AlbertSabirzianov/rest-newsletter.git
```
перейти в директорию docker
```commandline
cd rest-newsletter/docker
```
запустить
```commandline
docker compose up
```
документация будет доступна по адресу
```commandline
http://localhost:8000/docs 
```
остановить сервис
```commandline
docker compose down
```
# Настройки
Есть возможность настроить поведение сервиса при неудачной попытке отправки сообщения.
Все неудачные попытки отправки сообщения подписчику фиксируются, и их можно получить -
подробнее можно посмотреть здесь (можно посмотреть запустив сервис):
```commandline
http://localhost:8000/docs#/default/get_all_sending_errors_api_sending_errors_get
```
При неудачной попытке отправки сообщения плодписчику сервис может повторять попытки с 
определённой частотой пока сообщение не будет доставленно (будет получен код 200 в ответ),
для этого необходимо прописать в docker-compose.yml следущие переменные окружения
```yaml
services:
  app:
    image: albertsabirzianov/rest-newsletter:latest
    ports:
      - 8000:8000
    volumes:
      - ./../src/data:/app/data
    environment:
      - IS_REPEAT_SENDING=1 # флаг повторения попыток отправки
      - TIMEOUT_TO_REPEAT_IN_SECONDS=60 # частота повторения попыток в секундах
```













