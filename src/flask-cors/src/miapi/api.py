from flask import Flask
from flask_restful import Resource, Api#, reqparse

# Instantiate the app
app = Flask(__name__)
api = Api(app)

#parser = reqparse.RequestParser()
#parser.add_argument('task')

class MiAPI(Resource):
    def get(self):
        return {
            'data': ['data01', 'data02', 'data03', 'data04' ]
        }
    def post(self, *args, **kwargs):
        #args = parser.parse_args()
        return {
            'data': ['data05', 'data06', 'data07', 'data08' ]
        }

# Create routes
api.add_resource(MiAPI, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)