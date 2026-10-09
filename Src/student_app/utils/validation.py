
def validate_name(name):
    return bool(name.strip())


def validate_marks(marks):
    return 0 <= marks <= 100
