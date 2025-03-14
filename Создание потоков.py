import threading
from time import sleep, time
from datetime import timedelta

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

# Запуск функций последовательно
time_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time()
print(f"Работа функций {timedelta(seconds=time_end - time_start)}")

# Запуск функций в потоках
time_start = time()
threads = [
    threading.Thread(target=write_words, args=(10, 'example5.txt')),
    threading.Thread(target=write_words, args=(30, 'example6.txt')),
    threading.Thread(target=write_words, args=(200, 'example7.txt')),
    threading.Thread(target=write_words, args=(100, 'example8.txt'))
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

time_end = time()
print(f"Работа потоков {timedelta(seconds=time_end - time_start)}")
