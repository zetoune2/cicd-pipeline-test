import sys

sys.path.insert(0, './app')
from main import add, hello

def test_add():
    assert add(2, 3) == 5

def test_hello():
    assert hello("World") == "Hello, World!"
