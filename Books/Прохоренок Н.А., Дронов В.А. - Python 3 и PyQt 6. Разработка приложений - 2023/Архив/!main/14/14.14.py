class MyError(Exception): pass
try:
    raise MyError("Описание исключения")
except MyError as err:
    print(err)        # Выведет: Описание исключения
