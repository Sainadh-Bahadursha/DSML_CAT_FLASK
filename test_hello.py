from hello import app
import pytest

# this is like a server. We will call this when we want to call the server
@pytest.fixture
def client(): 
    return app.test_client
