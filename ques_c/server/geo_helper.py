import googlemaps
import geopy
from geopy.distance import geodesic

gmaps = googlemaps.Client(key='Your key here..')


def geocode(city):
    geocode_result = gmaps.geocode(city)
    location = geocode_result[0]['geometry']['location']

    return location.get('lat', 0), location.get('lng', 0)


def calc_distance(loc1: tuple, loc2: tuple):
    return geodesic(loc1, loc2).miles


def get_nearest_loc(target: tuple, cache_locations: list):

    distances = []
    all_dist_from_target = {}
    for cache_location in cache_locations:
        cache_dist_from_target = calc_distance(target, cache_location.coord)
        all_dist_from_target[cache_dist_from_target] = cache_location
        distances.append(cache_dist_from_target)

    distances.sort()

    smallest_distance = distances[0]
    nearest_cache_location = all_dist_from_target[smallest_distance]
    return nearest_cache_location


if __name__ == '__main__':
    locations = [(51.5073509, -0.1277583), (19.0759837, 72.8776559),
                 (43.653226, -79.3831843)]  # london, mumbai,toronto
    montreal_loc = (45.5016889, -73.567256)
    print(get_nearest_loc(montreal_loc, locations))
