from predictions import app
import pytest
import json

# this act like a server. We will call this when we want to call the server
@pytest.fixture
def client(): 
    with app.test_client() as client:
        yield client

# should check the response code is 200 - successful or not
# should check output of pinger - "I am pinging"
def test_pinger(client):
    resp = client.get("/ping")
    assert resp.status_code == 200
    assert resp.json == {"MESSAGE": "Hi I am Pinging"}
