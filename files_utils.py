import json
import yaml

# функция для чтения данных из json файла
def read_json(file_path: str, encoding: str = "utf-8"):
    """
    Читает данные из JSON-файла.
    Входные параметры:
    `file_path`: Путь к файлу.
    `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
    return: `data`: Данные, считанные из файла.
    """
    try: # попробуй прочитать
        with open(file_path, 'r', encoding=encoding) as file:
            data_to_read = json.load(file) # получаем данные из файла в переменную
        return print(data_to_read)
    # обработчики ошибок
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Ошибка при чтении JSON из файла {file_path}.")
        return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def write_json(data: dict, file_path: str, encoding: str = "utf-8"):
    """
    Записывает данные в JSON-файл.
    Входные параметры:
    `data`: Данные для записи.
    `file_path`: Путь к файлу.
    `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
    return `None`
    """
    try: # попробуй записать
        with open(file_path, 'w', encoding=encoding) as file: # открываем файл для записи
            json.dump(data, file, indent=4) # записываем данные в файл (dump - Записывает объект Python в файл в формате JSON.)
            print(f"Данные успешно записаны в файл: {file_path}")
    except Exception as e:
            print(f"Ошибка при записи данных в файл {file_path}: {e}")

data_to_write_json = [
        {
            "id": 1,
            "username": "alice_smith",
            "first_name": "Alice",
            "last_name": "Smith"
        },
        {
            "id": 2,
            "username": "bob_johnson",
            "first_name": "Bob",
            "last_name": "Johnson"
        },
        {
            "id": 3,
            "name": "John",
            "age": 30,
            "city": "New York"
        }
    ]

def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    """
    Добавляет данные в существующий JSON-файл.
    Входные параметры:
    `data`: Список словарей с данными для добавления.
    `file_path`: Путь к файлу.
    `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Нет.
    """
    try:
        # Попытка открыть существующий файл и загрузить данные
        with open(file_path, 'r', encoding=encoding) as file:
            existing_data = json.load(file)
            if not isinstance(existing_data, list):
                raise ValueError("Существующие данные в файле не являются списком.")
    except FileNotFoundError:
        # Если файл не существует, создаем новый список
        existing_data = []
    except json.JSONDecodeError:
        # Если файл пуст или содержит некорректные данные, создаем новый список
        existing_data = []

    # Добавляем новые данные в существующие
    existing_data.extend(data)
    # добавляем данные обратно в файл
    try:
        with open(file_path, 'a', encoding=encoding) as file:
            json.dump(existing_data, file, indent=4, ensure_ascii=False)
        print(f"Данные успешно добавлены в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи данных в файл {file_path}: {e}")

data_to_append_json = {
            "id": 3,
            "username": "alex_chern",
            "first_name": "Alex",
            "last_name": "Chern"
        }


# Функции для работы с CSV:
def read_csv(file_path, delimiter=';', encoding='windows-1251'):
    """
    Читает данные из CSV-файла без использования модуля csv.
    
    Входные параметры:
    `file_path`: Путь к файлу.
    `delimiter`: Разделитель полей в файле (по умолчанию `';'`).
    `encoding`: Кодировка файла (по умолчанию `"windows-1251"`).
    
    Возвращаемое значение: Список списков, представляющих строки данных из файла.
    """
    data = []
    
    try:
        with open(file_path, mode='r', encoding=encoding) as file:
            for line in file:
                # убираем лишние пробелы и символы перевода строки
                line = line.strip()
                # разделяем строку по разделителю
                row = line.split(delimiter)
                data.append(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    
    return data

def write_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    """
    Записывает данные в CSV-файл.
    
    Входные параметры:
    `data`: Данные для записи (список списков, где каждый внутренний список представляет строку).
    `file_path`: Путь к файлу.
    `delimiter`: Разделитель полей в файле (по умолчанию `';'`).
    `encoding`: Кодировка файла (по умолчанию `"windows-1251"`).
    
    Возвращаемое значение: Нет.
    """
    try:
        with open(file_path, mode='w', encoding=encoding) as file:
            for row in data:
                # Преобразуем каждое значение в строку и объединяем с разделителем
                line = delimiter.join(map(str, row))
                # Записываем строку в файл
                file.write(line + '\n')
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

data_to_write_csv = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
]

def append_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    """
    Добавляет данные в существующий CSV-файл.
    
    Входные параметры:
    `data`: Данные для добавления (список списков, где каждый внутренний список представляет строку).
    `file_path`: Путь к файлу.
    `delimiter`: Разделитель полей в файле (по умолчанию `';'`).
    `encoding`: Кодировка файла (по умолчанию `"windows-1251"`).
    
    Возвращаемое значение: Нет.
    """
    try:
        with open(file_path, mode='a', encoding=encoding) as file:
            for row in data:
                # Преобразуем каждое значение в строку и объединяем с разделителем
                line = delimiter.join(map(str, row))
                # Записываем строку в файл
                file.write(line + '\n')
    except Exception as e:
        print(f"Ошибка при добавлении данных в файл: {e}")

data_to_append_csv = [
    ['Charlie', 22, 'Chicago']
]

# Функции для работы с TXT:
def read_txt(file_path, encoding="utf-8"):
    """
    Читает данные из текстового файла.
    Входные параметры:
    `file_path`: Путь к файлу.
    `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Содержимое файла в виде строки.
    """
    try:
        with open(file_path, mode='r', encoding=encoding) as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_path}' не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def write_txt(data, file_path, encoding="utf-8"):
    """
    Записывает данные в текстовый файл.
    Входные параметры:
    `data`: Данные для записи (строка или список строк).
    `file_path`: Путь к файлу.
    `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Нет.
    """
    try:
        with open(file_path, mode='w', encoding=encoding) as file:
            if isinstance(data, list):
                # Если данные — это список строк, записываем их построчно
                for line in data:
                    file.write(line + '\n')
            else:
                # Если данные — это строка, записываем её как есть
                file.write(data)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

data_to_write_txt = "Это строка для записи в файл."

def append_txt(data, file_path, encoding="utf-8"):
    """
    Добавляет данные в конец текстового файла.
    Входные параметры:
    `data`: Данные для добавления (строка или список строк).
    `file_path`: Путь к файлу.
    `encoding`: Кодировка файла (по умолчанию `"utf-8"`).
    Возвращаемое значение: Нет.
    """
    try:
        with open(file_path, mode='a', encoding=encoding) as file:
            if isinstance(data, list):
                # Если данные — это список строк, добавляем их построчно
                for line in data:
                    file.write(line + '\n')
            else:
                # Если данные — это строка, добавляем её как есть
                file.write(data + '\n')
    except Exception as e:
        print(f"Ошибка при добавлении данных в файл: {e}")

data_to_append_txt = "Это строка для добавления в файл."



def main():
    print('выполнение main')
    read_json('test.json')
    write_json(data_to_write_json,'test.json')
    append_json(data_to_append_json, 'test.json')
    read_csv('test.csv')
    write_csv(data_to_write_csv, 'test.csv')
    append_csv(data_to_append_csv, 'test.csv')
    read_txt('test.txt')
    write_txt(data_to_write_txt, 'test.txt')
    append_txt(data_to_append_txt, 'test.txt')




if __name__ == '__main__':
    main()