from src.justins_function import justins_function

def test_justin1():
  assert(justins_function.add(10, 20) == 30)

def test_justin2():
  assert(justins_function.add(5, 60) == 65)

def test_justin3():
  assert(justins_function.add(1, 1) == 2)