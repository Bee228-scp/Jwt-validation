# JWT: наївна та сувора валідація (Flask)

Навчальний проект про те, чим відрізняється **прочитати** JWT-токен від **перевірити** його.

Два Flask-сервери на localhost приймають один і той самий токен, але перевіряють його по-різному:

| Сервер | Порт | Що робить |
|--------|------|-----------|
| Наївний (`naive_server.py`) | 5000 | Не перевіряє підпис (`verify_signature = False`) і вірить payload |
| Суворий (`strict_server.py`) | 5001 | Вимагає алгоритм HS256, дійсний підпис, `iss = lab7`, `aud = students`; будь-яка помилка дає 401 |

`make_token.py` видає тестові токени: коректний і підроблений (`alg = none`, `role = admin`, без підпису).

## Результати

- Коректний токен: обидва сервери повертають `200 OK`
- Підроблений токен (`role = admin`, `alg = none`): наївний сервер повірив і видав роль admin, суворий відхилив з `401 UNAUTHORIZED`
- Автоматичний набір перевірок `jwt_tool` (alg none, порожній і null-підпис, RSA key confusion, JWKS, kid injection): наївний сервер прийняв частину атак, суворий відхилив усі

## Висновок

Payload JWT це лише base64, його може прочитати будь-хто. Токен надійний тільки тоді, коли сервер перевіряє підпис із фіксованим алгоритмом та claims `iss`, `aud`, `exp`.

## Запуск

```
pip install -r requirements.txt
python strict_server.py      # порт 5001
python naive_server.py       # порт 5000 (в іншому терміналі)
```

Видати токен і надіслати запит (PowerShell):

```
$GOOD = python make_token.py good
curl.exe -i -X POST -H "Authorization: Bearer $GOOD" http://localhost:5001/api

$BAD = python make_token.py bad
curl.exe -i -X POST -H "Authorization: Bearer $BAD" http://localhost:5000/api
curl.exe -i -X POST -H "Authorization: Bearer $BAD" http://localhost:5001/api
```

## Важливо

Ключ підпису в коді записаний прямо в тексті, бо це навчальний стенд. У реальному проекті його беруть зі змінної середовища. Усі перевірки виконувались лише на власному локальному стенді.

## Технології

Python, Flask, PyJWT, jwt_tool, curl
