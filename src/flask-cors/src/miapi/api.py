from flask import Flask
from flask_restful import Resource, Api#, reqparse
from flask_cors import CORS

# Instantiate the app
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/miapi/*": {"origins": "*"}})
#parser = reqparse.RequestParser()
#parser.add_argument('task')

class MiAPI(Resource):
    def get(self):
        return {
            'cors':'Habilitado',
            'data': ['data01', 'data02', 'data03', 'data04' ]
        }
    def post(self, *args, **kwargs):
        #args = parser.parse_args()
        return {
            'cors':'Habilitado',
            'data': ['data05', 'data06', 'data07', 'data08' ]
        }

class MiAPI2(Resource):
    def get(self):
        return {
            'cors':'Deshabilitado',
            'data': ['data01', 'data02', 'data03', 'data04' ]
        }
    def post(self, *args, **kwargs):
        #args = parser.parse_args()
        return {
            'cors':'Deshabilitado',
            'data': ['data05', 'data06', 'data07', 'data08' ]
        }

# Create routes
api.add_resource(MiAPI, '/miapi/')
api.add_resource(MiAPI2, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)