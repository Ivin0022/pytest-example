def add(a, b):
    if not isinstance(a, int):
        raise ValueError("a needs to be a int")
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b
