import requests


def main():
    """
    Отправляет POST-запрос к JSONPlaceholder API для создания новой записи.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {'title': 'foo', 'body': 'bar', 'userId': 1}
    
    response = requests.post(url, json=data)
    
    print(f'Статус-код ответа: {response.status_code}')
    print('\nСодержимое ответа:')
    print(response.json())


if __name__ == '__main__':
    main()

