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

data_to_write = [
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

data_to_append = {
            "id": 3,
            "username": "alex_chern",
            "first_name": "Alex",
            "last_name": "Chern"
        }

def main():
    print('выполнение main')
    # read_json('test.json')
    # write_json(data_to_write,'test.json')
    append_json(data_to_append, 'test.json')



if __name__ == '__main__':
    main()