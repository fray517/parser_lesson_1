import requests


def main():
    """
    Отправляет GET-запрос к JSONPlaceholder API с фильтрацией по userId.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    params = {'userId': 1}
    
    response = requests.get(url, params=params)
    
    print(f'Статус-код ответа: {response.status_code}')
    print('\nПолученные записи:')
    
    posts = response.json()
    for post in posts:
        print(f'\nID: {post["id"]}')
        print(f'Заголовок: {post["title"]}')
        print(f'Текст: {post["body"]}')


if __name__ == '__main__':
    main()

