from files_utils import read_json, write_json, append_json, read_csv, write_csv, append_csv, read_txt, write_txt, append_txt, read_yaml


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

data_to_append_json = {
            "id": 3,
            "username": "alex_chern",
            "first_name": "Alex",
            "last_name": "Chern"
        }

data_to_write_csv = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
]

data_to_append_csv = [
    ['Charlie', 22, 'Chicago']
]

data_to_write_txt = "Это строка для записи в файл."

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
    read_yaml('test.yaml')

if __name__ == '__main__':
    main()