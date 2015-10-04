from bottle import route, run
import requests

@route('/')
def find():
    r = requests.get('http://www.omdbapi.com/?t=hannibal&y=&plot=short&r=json')
    return r.json()

run(host='localhost', port=8080, debug=True)