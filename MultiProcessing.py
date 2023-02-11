# Interpreter 3.7 -> 3.11

"Простой Python стр. 305 Процессы"


import multiprocessing  # имеет более богатый функционал, чем threading
import os


def doubler(number):
    """
    Функция умножитель на два
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(number, result, proc))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []
    for index, number in enumerate(numbers):
        proc = multiprocessing.Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
