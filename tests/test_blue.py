from microservices.blue.src.app import app
import json


class TestPaths():
    def test_health(self):
        '''
        This function does a GET on the path /health and
        validate if the response body has data and the status code.

        Test:
          assert response.status_code == 200
          assert data['status'] == 'up'
        '''
        response = app.test_client().get(
            '/health',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['status'] == 'up'

    def test_home(self):
        '''
        This function does a GET on the path / and
        validate if the response body has data and the status code.

        Test:
          assert response.status_code == 200
          assert data['name'] == 'blue'
        '''
        response = app.test_client().get(
            '/',
            content_type='application/json'
        )

        data = json.loads(response.get_data(as_text=True))

        assert response.status_code == 200
        assert data['name'] == 'blue'
