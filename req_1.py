import requests


def main():
    """
    Отправляет GET-запрос к GitHub API для поиска репозиториев с HTML.
    """
    url = 'https://api.github.com/search/repositories'
    params = {'q': 'language:html'}
    
    response = requests.get(url, params=params)
    
    print(f'Статус-код ответа: {response.status_code}')
    print('\nСодержимое ответа в формате JSON:')
    print(response.json())


if __name__ == '__main__':
    main()

