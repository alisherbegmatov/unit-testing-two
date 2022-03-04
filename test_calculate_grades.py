import unittest
from unittest import mock
import pytest
import math
from calculate_grades import *

def test_display_grade_stat():
    grade_list = [10, 20, 30, 40, 50]
    mean, standard_deviation = calculate_stat(grade_list)
    assert math.isclose(mean, 30.0)
    assert math.isclose(standard_deviation, 14.142135623730951)
