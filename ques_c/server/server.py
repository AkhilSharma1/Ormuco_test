from aiohttp import web
import socketio
from server import *
from geo_helper import *
from cache_location import CacheLocation

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

cache_locations = []


@sio.event
def connect(sid, environ):
    pass



@sio.event
async def is_cache(sid, data):
    print('new cache' + str(data))
    city = data['city']
    connection_url = data['addr']
    coord = geocode(city)
    cache_location = CacheLocation(city, connection_url, coord)
    cache_locations.append(cache_location)
    sio.enter_room(sid, "caches")


@sio.event
async def data(sid, data):
    print("sending to all caches: ", data)
    await sio.emit('receive_data_from_server', data=data, room="caches", skip_sid=sid)


@sio.event
async def del_data(sid, key):
    print("key to be deleted ", key)
    await sio.emit('delete', data=key, room="caches", skip_sid=sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)
    sio.leave_room(sid, "caches")


async def handle(request):
    client_city = request.rel_url.query['city']
    client_city_coord = geocode(client_city)

    nearest_cache_loc: CacheLocation = get_nearest_loc(
        client_city_coord, cache_locations)
    cache_str = str(nearest_cache_loc)
    print('sending data to client:'+cache_str)
    return web.Response(text=cache_str)

app.router.add_get('/', handle)


if __name__ == '__main__':
    web.run_app(app)
