import json

from flask import Flask
from flask_restx import Api, reqparse, Resource


# Instantiate our Flask API
app = Flask(__name__)
api = Api(app)


# For parsing query arguments
parser = reqparse.RequestParser()


@api.route('/issues')
class Issues(Resource):

    @api.doc(params={'data': {'description': 'JSON data payload'}})
    def put(self):
        '''
        Accept a JSON object and print/log the object
        '''
        parser.add_argument('data', type=str)
        args = parser.parse_args()
        print(args)

        try:
            _response = json.loads(args.data)
        except:
            _response = "Invalid value for data, must be a valid JSON string"
 
        response = _response

        return response

    @api.doc(params={'id': {'description': 'Issue ID to fetch'},})
    def get(self):
        '''
        Return a static JSON object
        '''
        parser.add_argument('id', type=int)
        args = parser.parse_args()

        response = {
            'id': args.id,
            'title': 'My issue',
            'description': 'This is an issue.'
        } 
        
        return response 

    @api.marshal_with(model, envelope='resource')
    def post(self):
        '''
        Accept a JSON object and print/log the object
        '''
        parser.add_argument('data', type=str)
        args = parser.parse_args()

        try:
            _response = json.loads(args.data)
        except:
            _response = "Invalid value for data, must be a valid JSON string"
       
        response = _response

        return response

    @api.doc(params={'id': {'description': 'Issue ID to delete'},})
    def delete(self):
        '''
        Print/log out the object or ID to delete
        '''
        parser.add_argument('id', type=int)
        args = parser.parse_args()

        response = args.id

        return response


if __name__ == '__main__':
    app.run(debug=True)