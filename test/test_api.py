import unittest
import json
from app import app

class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        # Given
        with app.test_client() as client:
            # When
            response = client.post('/ner', json={'sentence': 'Portugal and Spain share a border in Europe'})
            # Then
            assert response.status_code == 200


    def test_ner_endpoint_given_json_body_with_known_entities_returns_entity_result_in_response(self):
        # Given
        with app.test_client() as client:
            # When
            response = client.post('/ner', json={'sentence': 'Albert Einstein'})
            # Then
            data = json.loads(response.data)
            assert len(data['entities']) > 0
            assert data['entities'][0]['ent'] == 'Albert Einstein'
            assert data['entities'][0]['label'] == 'Person'
