import socketio
from cache_lru import LRUCache
import argparse
from aiohttp import web


sio = socketio.Client()
cache = LRUCache()

serv_sio = socketio.AsyncServer()


@sio.event
def connect():
    print('connection to central server established')
    sio.emit('is_cache', data={'city': args.city, 'addr': args.addr})


@sio.event
def receive_data_from_server(data):
    print('data received from other caches ', data)
    cache.put(data[0], data[1])
    print('cache size is now :' + str(cache.size()))
    print(cache.storage)
    print('Enter key and value to store in cache as key:value')


@sio.event
def receive_data_from_server(data):
    print('data received from other caches ', data)
    cache.put(data[0], data[1])
    print('cache size is now :' + str(cache.size()))
    print(cache.storage)
    print('Enter key and value to store in cache as key:value')


@sio.event
def del_data(data):
    print('data to be deleted for key ', data)
    cache.delete(data)


def send_data(k, v):
    sio.emit('data', [k, v])


@sio.event
def disconnect():
    print('disconnected from central server')


@serv_sio.event
async def receive_data_from_client(sid, data):

    print('received from client'+str(data))
    send_data(data[0], data[1])


@serv_sio.event
def connect(sid, environ):
    print('connection established with a client')


parser = argparse.ArgumentParser(description='Set up a cache')
parser.add_argument(
    'city', type=str, help='city where this cache is running (for geolocation)')
parser.add_argument(
    'addr', type=str, help='address of the cache:(example: http://localhost:9090) ')
args = parser.parse_args()


if __name__ == '__main__':

    sio.connect('http://localhost:8080')
    app = web.Application()

    serv_sio.attach(app)
    port = args.addr.split(":")[2]
    # print(port)

    web.run_app(app, port=port)



