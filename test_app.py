# test_hello.py
from app import app

def test_app():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b"<h3>Welcome Guest !! You have opened Shubhi's Home Page</h3>"
