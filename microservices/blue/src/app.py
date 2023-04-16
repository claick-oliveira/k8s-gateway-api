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
      "name": 'blue'
    }
    '''
    return make_response(jsonify(
      {
        'name': 'blue',
        'pod': os.getenv('POD_NAME', 'blue'),
        'namespace': os.getenv('POD_NAMESPACE', 'blue'),
        'ip': os.getenv('POD_IP', '0.0.0.0'),
        'uuid': os.getenv('UUID', '7d226e7d-3c97')
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
    app.run(host='0.0.0.0', port=5001)