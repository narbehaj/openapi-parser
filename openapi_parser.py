import requests
import sys


def get_url_input():
    if len(sys.argv) < 2:
        print('No URL specified')
        sys.exit(1)

    else:
        import re
        # Django URL checker
        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(regex, sys.argv[1]) is not None:
            return sys.argv[1]
        else:
            print('Invalid URL - Ex: http://www.example.com/swagger.json')
            sys.exit(1)


def get_content(url):
    r = requests.get(url)
    try:
        return r.json()
    except:
        print('Could not parse the JSON URL. Might be incorrect URL.')
        sys.exit(1)


def parse_json(api_json):
    api_paths = []
    for path, value in api_json['paths'].items():
        api_paths.append(path)

    print('Swagger Version: {}'.format(api_json['swagger']))
    print('API Title: {}'.format(api_json['info']['title']))
    print('Version: {}'.format(api_json['info']['version']))
    print('Description: {}'.format(api_json['info']['description']))
    print('Host: {}'.format(api_json['host']))
    print('API Path: {}'.format(api_json['basePath']))
    print('Paths:')
    for path in api_paths:
        print('\t- {}'.format(path))


api_json = get_content(get_url_input())
parse_json(api_json)

