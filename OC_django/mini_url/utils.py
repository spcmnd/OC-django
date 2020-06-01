import random
import string


def generate(char_count):
    chars = string.ascii_letters + string.digits
    random_chars = [random.choice(chars) for _ in range(char_count)]

    return ''.join(random_chars)
