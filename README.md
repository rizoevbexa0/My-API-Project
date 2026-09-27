# Task Management API

REST API на FastAPI для управления задачами.

## Стек
Python, FastAPI, SQLAlchemy, Pydantic

## Структура
- models — модели базы данных
- schemas — Pydantic-схемы для валидации
- repository — слой работы с базой данных
- routers — маршруты API

## Запуск
pip install -r requirements.txt
uvicorn main:app --reload
