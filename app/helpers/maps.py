import json
from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps, Map

def index():
    # json_data = request.get_json(silent=True)
    # get json request
    devices_data = {} # dict to store data of devices
    devices_location = {}
    json_data = { # for testing
        'user' : {
            'x' : -34.9100807,
            'y' : -57.9417491,
        },
        'devices' : [
            {
                'id' : '0001',
                'x' : -34.9100807,
                'y' : -57.9417491,
                'data' : 'Centro test'
            }
        ]
    }

    user_location = (json_data['user']['x'], json_data['user']['y'])
    # json example : { 'user' : { 'x' : '300' , 'y' : '300' } }
    # get user_location from json & store as turple (x, y)

    devices_data[str(json_data['devices'][0]['id'])] = (
        json_data['devices'][0]['data']
    )

    devices_location[str(json_data['devices'][0]['id'])] = (
        json_data['devices'][0]['x'],
        json_data['devices'][0]['y']
    )
    # json example : { 'devices' : { 'id' : '0001', x' : '500', 'y' : '500' }, { ... } }
    # get device_location from json & store turple (x, y) in dictionary with device id as key
    # use for statements or something to get more locations from more devices

    circle = { # draw circle on map (user_location as center)
        'stroke_color': '#0000FF',
        'stroke_opacity': .5,
        'stroke_weight': 5,
        # line(stroke) style
        'fill_color': '#FFFFFF',
        'fill_opacity': .2,
        # fill style
        'center': { # set circle to user_location
            'lat': user_location[0],
            'lng': user_location[1]
        },
        'radius': 500 # circle size (50 meters)
    }

    map = Map(
        identifier = "map", varname = "map",
        # set identifier, varname
        lat = user_location[0], lng = user_location[1],
        # set map base to user_location
        zoom = 15, # set zoomlevel
        markers = [
            {
                'lat': devices_location['0001'][0],
                'lng': devices_location['0001'][1],
                'infobox': devices_data['0001']
            }
        ],
        # set markers to location of devices
        circles = [circle] # pass circles
    )

    return map


def showLoc(lat, long):
    # json_data = request.get_json(silent=True)
    # get json request
    devices_data = {} # dict to store data of devices
    devices_location = {}
    json_data = { # for testing
        'user' : {
            'x' : lat,
            'y' : long,
        },
        'devices' : [
            {
                'id' : '0001',
                'x' : lat,
                'y' : long,
                'data' : 'Centro test'
            }
        ]
    }

    user_location = (json_data['user']['x'], json_data['user']['y'])
    # json example : { 'user' : { 'x' : '300' , 'y' : '300' } }
    # get user_location from json & store as turple (x, y)

    devices_data[str(json_data['devices'][0]['id'])] = (
        json_data['devices'][0]['data']
    )

    devices_location[str(json_data['devices'][0]['id'])] = (
        json_data['devices'][0]['x'],
        json_data['devices'][0]['y']
    )
    # json example : { 'devices' : { 'id' : '0001', x' : '500', 'y' : '500' }, { ... } }
    # get device_location from json & store turple (x, y) in dictionary with device id as key
    # use for statements or something to get more locations from more devices

    circle = { # draw circle on map (user_location as center)
        'stroke_color': '#0000FF',
        'stroke_opacity': .5,
        'stroke_weight': 5,
        # line(stroke) style
        'fill_color': '#FFFFFF',
        'fill_opacity': .2,
        # fill style
        'center': { # set circle to user_location
            'lat': user_location[0],
            'lng': user_location[1]
        },
        'radius': 500 # circle size (50 meters)
    }

    map = Map(
        identifier = "map", varname = "map",
        # set identifier, varname
        lat = user_location[0], lng = user_location[1],
        # set map base to user_location
        zoom = 15, # set zoomlevel
        markers = [
            {
                'lat': devices_location['0001'][0],
                'lng': devices_location['0001'][1],
                'infobox': devices_data['0001']
            }
        ],
        # set markers to location of devices
        circles = [circle] # pass circles
    )

    return map
