from flask import Flask
import sys
import requests
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)
BASE = 'https://api.github.com/repos'

class Repository(Resource):
    def get(self, owner, repositoryName):
        queryUrl = BASE + '/' + owner + '/' + repositoryName
        print(queryUrl)
        response = requests.get(queryUrl)
        json = response.json()
        queryOutput = {
            'fullName': str(json.get('full_name')),
            'description': str(json.get('description')),
            'cloneURL': str(json.get('clone_url')),
            'stars': str(json.get('stargazers_count'))
            }
        print(queryOutput)
        return queryOutput

api.add_resource(Repository, '/repository/<string:owner>/<string:repositoryName>')

#for debugging
#if __name__ == '__main__':
#    app.run(debug=True)
