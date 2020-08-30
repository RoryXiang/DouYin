import requests

url = 'http://127.0.0.1:8000/groupr/'

data = {
    'req_data':111122
}
req = requests.post(url, data=data)

