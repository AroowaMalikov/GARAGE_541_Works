class ArrayList:
    def __init__(self, capacity=4) -> None:
        self._data = [None] * capacity  # внутренний массив фиксированного размера
        self._size = 0                  # текущее количество элементов
        self._capacity = capacity       # текущая вместимость

    def _resize(self, new_capacity: int) -> None:
        """Увеличивает/уменьшает вместимость внутреннего массива."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, value) -> None:
        """Добавляет элемент в конец массива."""
        if self._size == self._capacity:
            self._resize(max(1, self._capacity * 2)) # удваиваем при переполнении
        self._data[self._size] = value
        self._size += 1

    def insert(self, index: int, value) -> None:
        """Вставляет элемент по указанному индексу, сдвигая последующие вправо."""
        if index < 0 or index > self._size:
            raise IndexError("index out of range")
        if self._size == self._capacity:
            self._resize(max(1, self._capacity * 2))
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def get(self, i: int):
        """Возвращает элемент по индексу."""
        if i < 0 or i >= self._size:
            raise IndexError("index out of range")
        return self._data[i]

    def remove(self, i: int):
        """Удаляет элемент по индексу i и возвращает его."""
        if i < 0 or i >= self._size:
            raise IndexError("index out of range")
        removed = self._data[i]
        for j in range(i, self._size - 1):
            self._data[j] = self._data[j + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return removed

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"ArrayList({[self._data[i] for i in range(self._size)]})"


class DNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def append(self, value) -> None:
        """Добавляет элемент в конец списка."""
        new_node = DNode(value, prev=self._tail, next=None)
        if self._tail is None:  # список пуст
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def insert(self, index: int, value) -> None:
        """Вставляет элемент по индексу."""
        if index < 0 or index > self._size:
            raise IndexError("index out of range")

        if index == self._size:
            self.append(value)
            return

        if index == 0:
            new_node = DNode(value, prev=None, next=self._head)
            if self._head:
                self._head.prev = new_node
            self._head = new_node
            if self._tail is None:
                self._tail = new_node
            self._size += 1
            return

        # Находим узел на позиции index
        cur = self._head
        for _ in range(index):
            cur = cur.next

        prev_node = cur.prev
        new_node = DNode(value, prev=prev_node, next=cur)
        prev_node.next = new_node
        cur.prev = new_node
        self._size += 1

    def get(self, i: int):
        """Возвращает значение элемента по индексу."""
        if i < 0 or i >= self._size:
            raise IndexError("index out of range")

        # Идём с той стороны, где ближе
        if i < self._size // 2:
            cur = self._head
            for _ in range(i):
                cur = cur.next
        else:
            cur = self._tail
            for _ in range(self._size - 1 - i):
                cur = cur.prev
        return cur.value

    def remove(self, i: int):
        """Удаляет элемент по индексу i и возвращает его значение."""
        if i < 0 or i >= self._size:
            raise IndexError("index out of range")

        # Находим удаляемый узел
        if i < self._size // 2:
            cur = self._head
            for _ in range(i):
                cur = cur.next
        else:
            cur = self._tail
            for _ in range(self._size - 1 - i):
                cur = cur.prev

        value = cur.value

        # Перестраиваем ссылки
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self._head = cur.next

        if cur.next:
            cur.next.prev = cur.prev
        else:
            self._tail = cur.prev

        self._size -= 1
        return value

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = []
        cur = self._head
        while cur:
            values.append(cur.value)
            cur = cur.next
        return f"DLinkedList({values})"


import bisect


class SortedArraySet:
    """Упорядоченное множество на основе отсортированного массива."""
    
    def __init__(self) -> None:
        self._data = []
    
    def add(self, value) -> None:
        """Добавляет элемент, сохраняя порядок. Игнорирует дубликаты."""
        idx = bisect.bisect_left(self._data, value)
        if idx < len(self._data) and self._data[idx] == value:
            return  # уже есть
        bisect.insort(self._data, value)
    
    def contains(self, value) -> bool:
        """Проверяет наличие элемента через бинарный поиск."""
        idx = bisect.bisect_left(self._data, value)
        return idx < len(self._data) and self._data[idx] == value
    
    def remove(self, value) -> bool:
        """Удаляет элемент. Возвращает True, если удалён, False если не найден."""
        idx = bisect.bisect_left(self._data, value)
        if idx < len(self._data) and self._data[idx] == value:
            self._data.pop(idx)
            return True
        return False
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"SortedArraySet({self._data})"
    
    def __iter__(self):
        return iter(self._data)


class UnsortedArraySet:
    """Неупорядоченное множество на основе обычного списка."""
    
    def __init__(self) -> None:
        self._data = []
    
    def add(self, value) -> None:
        """Добавляет элемент, если его ещё нет."""
        if value not in self._data:
            self._data.append(value)
    
    def contains(self, value) -> bool:
        """Проверяет наличие элемента через in."""
        return value in self._data
    
    def remove(self, value) -> bool:
        """Удаляет элемент. Возвращает True, если удалён, False если не найден."""
        try:
            idx = self._data.index(value)
            self._data.pop(idx)
            return True
        except ValueError:
            return False
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"UnsortedArraySet({self._data})"
    
    def __iter__(self):
        return iter(self._data)
