
from working import convert 
import pytest

def main():
  test_wrong_format()
  test_time()
  test_wrong_hour()
  test_wrong_minute()



def test_wrong_format():
  with pytest.raises(ValueError):
    convert('9:00 AM / 8:25 PM')

def test_time():
  assert convert('9 AM to 5 PM') == '09:00 to 17:00'
  assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_wrong_hour():
  with pytest.raises(ValueError):
    convert('9:54 AM to 14:45')

def test_wrong_minute():
  with pytest.raises(ValueError):
    convert('5:00 AM to 7:60')



if __name__ == "__main__":
    main()

    