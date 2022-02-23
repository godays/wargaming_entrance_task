class StaticCyclicFifo:
    def __init__(self, capacity):
        self.capacity = capacity
        self.begin = 0
        self.end = 0
        self.data = [None] * self.capacity
        self.size = 0

    def next_pos(self, index):
        return (index + 1) % self.capacity

    def push(self, element):
        if self.size != 0 and self.begin == self.end:
            raise OverflowError

        self.size += 1
        self.data[self.end] = element
        self.end = self.next_pos(self.end)

    def pop(self):
        if self.size == 0:
            return None

        self.size -= 1
        element_to_return = self.data[self.begin]
        self.begin = self.next_pos(self.begin)
        return element_to_return


class DynamicCyclicFifo:
    def __init__(self):
        self.capacity = 1
        self.data = [None] * self.capacity
        self.size = 0
        self.begin = 0
        self.end = 0

    def next_pos(self, index):
        return (index + 1) % self.capacity

    def push(self, element):
        self.ensure_capacity()
        self.size += 1
        self.end = self.next_pos(self.end)
        self.data[self.end] = element

    def pop(self):
        if self.size == 0:
            return None

        self.size -= 1
        value = self.data[self.begin]
        self.begin = self.next_pos(self.begin)
        self.decrease_capacity()
        return value

    def ensure_capacity(self):
        if self.size == self.capacity:
            data_new = [None] * (self.capacity * 2)
            for i in range(self.size):
                data_new[i] = self.data[(self.begin + i) % self.capacity]
            self.data = data_new
            self.capacity *= 2
            self.begin = 0
            self.end = self.size - 1

    def decrease_capacity(self):
        if self.capacity <= 1:
            self.capacity = 1
            return
        if self.size <= (self.capacity // 2):
            data_new = [None] * (self.capacity // 2)
            for i in range(self.size):
                data_new[i] = self.data[(self.begin + i) % self.capacity]
            self.data = data_new
            self.capacity //= 2
            self.begin = 0
            self.end = self.size - 1
