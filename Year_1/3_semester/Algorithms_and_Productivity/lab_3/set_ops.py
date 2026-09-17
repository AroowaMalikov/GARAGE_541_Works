"""Формат строки операций: a5a7a10r7c5c7c10 или add5add7remove7contains5.

Коды операций: a/add — добавить, r/remove — удалить, c/contains — проверить наличие.
После кода идёт целое число (может быть со знаком минус).
"""

from structures import UnsortedArraySet

# Словарь соответствия кода операции и её названия для вывода
OP_NAMES = {
    "a": "добавлен",
    "add": "добавлен",
    "r": "удален",
    "remove": "удален",
    "c": "найден",
    "contains": "найден",
}


def parse_ops(line: str) -> list:
    """Разбирает строку формата a5r7c10 в список пар (код, число)."""
    ops = []
    i = 0
    while i < len(line):
        # Пробуем сначала длинные коды (add/remove/contains), потом короткие (a/r/c)
        matched = False
        for code in ("contains", "remove", "add", "a", "r", "c"):
            if line.startswith(code, i):
                i += len(code)
                # Считываем число (возможен минус)
                num_start = i
                if i < len(line) and line[i] == "-":
                    i += 1
                while i < len(line) and line[i].isdigit():
                    i += 1
                ops.append((code, int(line[num_start:i])))
                matched = True
                break
        if not matched:
            raise ValueError(f"Неверный формат в позиции {i}: '{line[i:]}'")
    return ops


def execute(line: str, verbose=True) -> list:
    """Выполняет операции из строки над множеством, возвращает строки-результаты."""
    s = UnsortedArraySet()
    results = []
    for code, value in parse_ops(line):
        if code in ("a", "add"):
            s.add(value)
            results.append(f"{value} добавлен")
        elif code in ("r", "remove"):
            removed = s.remove(value)
            results.append(f"{value} удален" if removed else f"{value} не найден")
        else:
            found = s.contains(value)
            results.append(f"{value} найден" if found else f"{value} не найден")
    if verbose:
        print(", ".join(results))
    return results


def main():
    print("Введите строку операций (например a5a7a10r7c5c7c10),")
    print("или имя файла, начинающееся с 'file:' (например file:ops.txt)")
    line = input("> ").strip()

    if line.startswith("file:"):
        with open(line[5:], encoding="utf-8") as f:
            line = f.read().strip()

    execute(line)


if __name__ == "__main__":
    main()
