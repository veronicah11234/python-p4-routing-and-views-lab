import io
import sys
import pytest
from app import app 

@pytest.fixture
def client():
    """Create a test client using the Flask application."""
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test the index route."""
    response = client.get('/')
    assert b"<h1>Python Operations with Flask Routing and Views</h1>" in response.data

def test_print_route(client):
    '''has a resource available at "/print/<parameter>".'''
    response = client.get('/print/hello')
    assert(response.status_code == 200)

def test_print_text(client):
    '''displays text of route in browser.'''
    response = client.get('/print/hello')
    assert(response.data.decode() == 'hello')

def test_print_text_in_console(client):
    '''displays text of route in console.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    client.get('/print/hello')
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == 'hello\n')

def test_count_route(client):
    '''has a resource available at "/count/<parameter>".'''
    response = client.get('/count/5')
    assert(response.status_code == 200)

def test_count_range_10(client):
    '''counts through range of parameter in "/count/<parameter" on separate lines.'''
    response = client.get('/count/10')
    count = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
    print("Expected count:", count)
    print("Actual response:", response.data.decode())
    assert response.data.decode().strip() == count.strip()


def test_math_route(client):
    '''has a resource available at "/math/<parameters>".'''
    response = client.get('/math/5/+/5')
    assert(response.status_code == 200)

def test_math_add(client):
    '''adds parameters in "/math/" resource when operation is "+".'''
    response = client.get('/math/5/+/5')
    assert(response.data.decode() == '10')

def test_math_subtract(client):
    '''subtracts parameters in "/math/" resource when operation is "-".'''
    response = client.get('/math/5/-/5')
    assert(response.data.decode() == '0')

def test_math_multiply(client):
    '''multiplies parameters in "/math/" resource when operation is "*".'''
    response = client.get('/math/5/*/5')
    assert(response.data.decode() == '25')

def test_math_divide(client):
    '''divides parameters in "/math/" resource when operation is "div".'''
    response = client.get('/math/5/div/5')
    assert(response.data.decode() == '1.0')

def test_math_modulo(client):
    '''finds remainder of parameters in "/math/" resource when operation is "%".'''
    response = client.get('/math/5/mod/5')  
    assert response.data.decode() == '0'  

