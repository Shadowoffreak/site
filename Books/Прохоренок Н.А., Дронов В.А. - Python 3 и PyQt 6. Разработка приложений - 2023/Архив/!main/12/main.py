# Доступ к модулю folder1\module1.py
import folder1.module1 as m1          # Выведет: __init__ из folder1
print(m1.msg)                         # Выведет: Модуль folder1.module1
from folder1 import module1 as m2
print(m2.msg)                         # Выведет: Модуль folder1.module1
from folder1.module1 import msg
print(msg)                            # Выведет: Модуль folder1.module1

# Доступ к модулю folder1\folder2\module2.py
import folder1.folder2.module2 as m3  # Выведет: __init__ из folder1.folder2
print(m3.msg)                         # Выведет: Модуль folder1.folder2.module2
from folder1.folder2 import module2 as m4
print(m4.msg)                         # Выведет: Модуль folder1.folder2.module2
from folder1.folder2.module2 import msg
print(msg)                            # Выведет: Модуль folder1.folder2.module2

input()
