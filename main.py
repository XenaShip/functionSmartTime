import time

class SmartTime:

    def __init__(self, n = 1):
        # время старта, первый вызов, определяется при создании объекта класса
        self.start_time = time.time()
        self.last_time = self.start_time
        # временное окно
        self.n = n
        # список для хранения предыдущих вызовов
        self.q = []


    def get_time(self):
      current = time.time()
      # запасная переменная для хранение временного окна, для изменения в отдельном случае
      wind = self.n
      if self.last_time >= current:
        while self.q[0] < self.last_time - self.n:
            # убираем прошедшие вызовы(за пределами временного окна)
          self.q.pop(0)
        if current - self.start_time < self.n:
        # изменение окна в случае, если с первого вызова не прошло достаточно времени
          wind = current - self.start_time
        current = self.last_time + wind / (len(self.q) + 1)
      # обновление последнего вызова
      self.last_time = current
      # сохраняем последний вызов в список
      self.q.append(self.last_time)
      return current
