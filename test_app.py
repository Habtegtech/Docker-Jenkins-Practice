# test_app.py
from app import app  # Import your Flask app

def test_hello_world():
    # Test if the root route returns "Hello world"
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data == b'Hello world'