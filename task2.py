# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print(f"X | Y | Z | ¬(X ∧ Y) ∨ Z")

for X in range(0, 2):
    for Y in range(0, 2):
        for Z in range(0, 2):
            data = not (X and Y) or Z
            print(f"{X} | {Y} | {Z} | {int(not (X and Y) or Z)}")