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

