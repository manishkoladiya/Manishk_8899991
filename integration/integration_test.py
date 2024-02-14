import pytest
from tenth_result import calculate_total, calculate_average, calculate_percentage

# Test case 1: All marks are above passing marks
def test_all_marks_above_passing():
    subject_marks = [85, 90, 75, 80, 70]
    assert calculate_total(subject_marks) == 400
    assert calculate_average(subject_marks) == 80
    assert calculate_percentage(400, 500) == 80

# Test case 2: Some marks are below passing marks
def test_some_marks_below_passing():
    subject_marks = [65, 70, 80, 75, 60]
    assert calculate_total(subject_marks) == 350
    assert calculate_average(subject_marks) == 70
    assert calculate_percentage(350, 500) == 70

# Test case 3: All marks are above 90
def test_all_marks_above_90():
    subject_marks = [95, 95, 95, 95, 95]
    assert calculate_total(subject_marks) == 475
    assert calculate_average(subject_marks) == 95
    assert calculate_percentage(475, 500) == 95

# Test case 4: All marks are 0
def test_all_marks_zero():cd
    subject_marks = [0, 0, 0, 0, 0]
    assert calculate_total(subject_marks) == 0
    assert calculate_average(subject_marks) == 0
    assert calculate_percentage(0, 500) == 0
