from student_app.utils.validation import validate_name, validate_marks

def test_valid_name():
    assert validate_name("Ali") is True

def test_invalid_name():
    assert validate_name("   ") is False

def test_valid_marks():
    assert validate_marks(85) is True

def test_invalid_marks_above_100():
    assert validate_marks(110) is False

def test_invalid_marks_below_0():
    assert validate_marks(-5) is False

def test_valid_marks_zero():
    assert validate_marks(0) is True
