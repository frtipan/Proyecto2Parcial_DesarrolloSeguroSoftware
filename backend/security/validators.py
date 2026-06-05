def validate_code(code):

    if code is None:
        return False

    if not isinstance(code, str):
        return False

    if len(code.strip()) == 0:
        return False

    if len(code) > 50000:
        return False

    return True