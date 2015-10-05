#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import bottle
from bottle import route, response, get, run
import requests

bottle.debug(True)

@get('/')
def index():
    res = requests.get("http://www.omdbapi.com/?t=game+of+thrones&y=&plot=short&r=json")
    return res.json()
run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))