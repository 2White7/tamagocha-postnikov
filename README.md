# Tamagocha

Простий консольний симулятор тамагочі на Python.

## Структура проєкту

- `tamagocha_pkg/model.py` — основна модель персонажа (клас `Tamagocha`)
- `tamagocha_pkg/storage.py` — читання/запис стану у `data.json`
- `tamagocha_pkg/timeutils.py` — обчислення "занепаду" показників у часі
- `tamagocha_pkg/interface.py` — консольний інтерфейс (введення/виведення)
- `main.py` — точка входу
- `tests/` — unit-тести

## Запуск

```
python main.py
```

## Тести

```
pytest
```
