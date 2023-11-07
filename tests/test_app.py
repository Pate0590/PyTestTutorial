# Import the 'app' instance from the app module which is our Flask application
from app import app
# Import the pytest library which will be used for writing and running our tests
import pytest

# Define a pytest 'fixture' which sets up any necessary configuration for our tests.
# This fixture named 'client' will be used by our tests to make requests to our application.
# Given part of the framework: the setup of our test client using a fixture.


@pytest.fixture
def client():
    # 'app.test_client()' creates a test client for our application.
    # This client can be used to simulate HTTP requests without running the server.
    # The test client is the initial context here.
    with app.test_client() as client:
        # 'yield' is used here to provide the test client to the test and then
        # clean up after the test is done. It's a way to enter and exit the test context.
        yield client
        # After the test is done, the code following the yield statement (if there is any)
        # would run as a form of cleanup.
        # This is a way to ensure that resources are properly released after the test is completed.

# Define a test function that will use the 'client' fixture.
# Pytest will automatically call any function named 'test_*' as a test case.
# This is our actual test case, following the Given-When-Then framework.


def test_home(client):
    # Given: The application is up and running.

    # When: We make a GET request to the home ('/') route.
    # Use the test client to make a request to the home route ('/') of our application.
    response = client.get('/')

    # Then: The expected response is a '200 OK' status and 'Hello, World!' text.

    # Assert that the response data matches the expected string 'Hello, World!'.
    # The 'b' prefix signifies a byte string.
    assert response.data == b"Hello, World!"
    # Assert that the response status code is 200, indicating a successful response.
    assert response.status_code == 200
