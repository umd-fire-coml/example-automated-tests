from src.bean_factory import BeanFactory

def test_get_beans():
    factory = BeanFactory(10)
    assert factory.get_beans() == 10

def test_add_bean():
    factory = BeanFactory(10)
    factory.cook_bean()
    assert factory.get_beans() == 11

def test_eat_bean():
    factory = BeanFactory(10)
    factory.eat_bean()
    assert factory.get_beans() == 9

