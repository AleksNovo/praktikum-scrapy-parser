# Асинхронный парсер PEP

Парсер собирает информацию со страницы https://peps.python.org/

## Запуск проекта
Клонируйте репозиторий:
```
git@github.com:AleksNovo/scrapy_parser_pep.git
```

Создайте виртуальное окружение и установите зависимости.
```
python -m venv venv
```
```
pip install -r requirements.txt
```
запустите паука при помощи команды:
```
scrapy crawl pep
```