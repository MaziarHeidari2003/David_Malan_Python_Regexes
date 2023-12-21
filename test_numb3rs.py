from numb3rs import validate
import pytest


def format_test():
  assert validate(r'1.2.3.4') == True
  assert validate(r'1.2.3') == False
  assert validate(r'1.2') == False
  assert validate(r'1') == False

def amount_test():
  assert validate(r'1.512.155.155') == False
  assert validate(r'255.255.255.255') == True

