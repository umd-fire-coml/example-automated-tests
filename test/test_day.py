from src.whatdayisit import Day

def test_get_day():
  assert(Day.getDay() != "22nd of September")

def test_get_day2():
    assert(Day.getDay() == "21st of September")