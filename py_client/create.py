import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

data = {
    'title': 'This field is done',
    'content': 'Something new',
    'price': 29.99,
}
get_response = requests.post(endpoint, data=data)
print(get_response.json())
