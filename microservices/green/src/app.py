from flask import (
    Flask, jsonify, make_response
)
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route('/health', methods=['GET'])
def get_health():
    '''
    This function returns the service's status . The method
    allowed is GET

    Path:
    /health

    Returns:
    {
      "status": 'up'
    }
    '''
    return make_response(jsonify(
      {
        'status': 'up'
      }
    ), 200)


@app.route('/', methods=['GET'])
def get_home():
    '''
    This function returns the service's name . The method
    allowed is GET

    Path:
    /health

    Returns:
    {
      "name": 'green'
    }
    '''
    return make_response(jsonify(
      {
        'name': 'green',
        'pod': os.environ['POD_NAME'],
        'namespace': os.environ['POD_NAMESPACE'],
        'ip': os.environ['POD_IP'],
        'uuid': os.environ['UUID']
      }
    ), 200)


@app.errorhandler(404)
def not_found(error):
    '''
    This function returns a message as json.

    Parameters:
    error (err): Error message

    Returns:
    {
        'error': 'Not found'
    }
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(405)
def not_allowed(error):
    '''
    This function returns a message as json.

    Parameters:
    error (err): Error message

    Returns:
    {
        'error': 'Not found'
    }
    '''
    return make_response(jsonify({'error': 'Method Not Allowed'}), 405)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
