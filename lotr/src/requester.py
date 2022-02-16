import requests

scheme = {
    "book": {
        "endpoint": "book/",
        "specific": "/chapter"
    },
    "movie":{
        "endpoint": "movie/",
        "specific": "/quote"
    },
    "character": {
        "endpoint": "character/",
        "specific": "/quote"
    },
    "quote": {
        "endpoint": "/quote",
        "specific": None,
    },
    "chapter": {
        "endpoint": "/chapter",
        "specific": None
    }
}

def build_path(type, id=None, specific=False):
    route = scheme[type]
    if id == None:
        path = route['endpoint']
    else:
        path = (route['endpoint'] + id + route['specific'] if specific == True else route['endpoint'] + id)
    print(path)
    return path

def call(path, auth=None, **options):
    headers = {
         'Content-Type': 'application/json'
    }
    if auth != None:
        headers = {
        'Authorization': ('Bearer ' + auth),
        'Content-Type': 'application/json',
        }

    r = requests.get(
        'https://the-one-api.dev/v2/' + path,
        params=options,
        headers=headers
    )

    response = r.json()

    return response
