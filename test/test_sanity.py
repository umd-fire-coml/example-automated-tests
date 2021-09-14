import pytest

def test_sanity():
  assert(1 == 1)

@pytest.mark.xfail
def test_sanity_fail():
  assert(1 == 0)
