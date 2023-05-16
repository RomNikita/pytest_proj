def get_val(collection, key, default='git'):
    """Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default."""

    for i, value in collection.items():
        if key == i:
            return value
        elif key != i:
            return default
    if collection == {}:
        return default

