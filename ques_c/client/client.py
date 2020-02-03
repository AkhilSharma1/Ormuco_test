import socketio
import argparse
import requests
import json


sio = socketio.Client()
# cache_url = None
server_url = 'http://localhost:8080'


def get_cache_data():
    # global cache_url
    resp = requests.get(url=server_url, params={"city": args.city})
    cache_data = json.loads(resp.text.replace("'", '"'))
    print(
        f'nearest cache is located at {cache_data["city"]} : {cache_data["connection_url"]}')
    cache_url = cache_data['connection_url']
    connect_cache(cache_url)


def connect_cache(cache_url):
    sio.connect(cache_url)
    # sio.wait()


def update_cache(k, v):
    sio.emit('receive_data_from_client', [k, v])


parser = argparse.ArgumentParser(description='Set up a client')
parser.add_argument(
    'city', type=str, help='city where this client is running (for geolocation)')

args = parser.parse_args()
get_cache_data()

while True:
    print('Enter key and value to send to connected cache as key:value')
    k, v = input().split(':')

    update_cache(k, v)
