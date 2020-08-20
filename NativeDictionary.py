class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.value = [None] * self.size


    def hash_fun(self, key):
        """hash-функция"""
        p = 0.33
        summ = 0
        result = None

        for i in key:
            summ += ord(i) * p

        result = int(summ % self.size)
        return result


    def is_key(self, key):
        """Поиск ключа"""
        found_key = False

        if key in self.slots:
            found_key = True

        return found_key


    def put(self, key, value):
        """Запись значения по ключу"""
        self.slots[self.hash_fun(key)] = key
        self.value[self.hash_fun(key)] = value


    def get(self, key):
        """Получение значения по ключу"""
        found_value = None

        if self.is_key(key):
            found_value = self.value[self.hash_fun(key)]

        return found_value
