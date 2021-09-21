from src.goodbye import Goodbye

def test_get_goodbye():
  assert(Goodbye.getGoodbye() == "Goodbye World")
