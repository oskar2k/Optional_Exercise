import calculator
import math
import pytest

def test_add_exercise_1():
    assert calculator.add(5, 10) == 15

def test_add_exercise_1b():
    assert calculator.add(15, 15) == 30