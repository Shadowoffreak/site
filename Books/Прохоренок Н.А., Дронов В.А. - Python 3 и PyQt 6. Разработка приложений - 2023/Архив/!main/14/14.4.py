try:
    x = 1 / 0                     # Ошибка деления на 0
except (NameError, IndexError, ZeroDivisionError) as err:
    print(err.__class__.__name__) # имя класса исключения
    print(err)                    # Текст сообщения об ошибке
