from src.hello import Hello

def test_get_hello():
  assert(Hello.getHello() == "Hello World")
