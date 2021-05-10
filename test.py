import requests

BASE = 'http://127.0.0.1:5000'

responsegit = requests.get(BASE + '/repository/twbs/bootstrap')

