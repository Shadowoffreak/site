import re
p = re.compile(r"[0-9]+", re.S)
if p.search("Строка245"):
    print("Число")            # Выведет: Число
else:
    print("Не число")
input()
