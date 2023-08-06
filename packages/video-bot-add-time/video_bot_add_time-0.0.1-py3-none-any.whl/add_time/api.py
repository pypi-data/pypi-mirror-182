from dotenv import load_dotenv
from os import environ

from flask import Flask
from flask import request
from flask_restful import Resource, Api  #, reqparse

from add_time.handler import handler
from add_time.utils.lambda_helpers import get_json
from add_time.get_event import get_event

app = Flask(__name__)

API_PORT = environ.get('API_PORT')
DEBUG = environ.get('DEBUG')

class Api:
    
    @app.route('/', defaults={'path': ''}, methods = ['GET', 'POST'])
    @app.route('/<path:path>', methods = ['GET', 'POST'])
    def catch_all(path):
        
        load_dotenv()
        
        event = request.json #get_event()
        
        event = {**event, 'path': '/' + path}

        result = handler(event, None)
        json_str = get_json(result)
        return json_str
         

    def run(self):
        app.run(debug=DEBUG, host='0.0.0.0', port = API_PORT)   


    

  








    

    
    
