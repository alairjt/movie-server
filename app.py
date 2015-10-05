#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import bottle
from bottle import default_app, route, response, get
import requests

bottle.debug(True)

@get('/')
def index():
    res = requests.get("http://www.omdbapi.com/?t=game+of+thrones&y=&plot=short&r=json")
    return res.json()
bottle.run(host='localhost', port=9090)