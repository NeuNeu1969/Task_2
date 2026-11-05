# Task_2: API-тесты Stellar Burgers

Автотесты API сервиса https://stellarburgers.education-services.ru (requests + pytest + Allure).

## Покрытие

- Создание пользователя
- Логин пользователя
- Изменение данных пользователя
- Создание заказа
- Получение заказов пользователя

## Структура

- `api/` классы-обёртки над ручками
- `tests/` тесты (по классу на ручку) и фикстуры в `conftest.py`
- `data.py`, `urls.py`, `constants.py`, `helpers.py` данные, адреса, константы, генерация данных
- `allure_results/` результаты для Allure-отчёта

## Запуск

```
pip install -r requirements.txt
pytest tests/ --alluredir=allure_results
allure serve allure_results
```

## Особенности стенда

- Заказ без авторизации создаётся (200), хотя в документации заказы доступны только авторизованным.
- Созданные заказы не удаляются: ручки удаления заказа нет.
