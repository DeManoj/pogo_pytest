import random
import string

def generate_random_number():
    return random.randint(0, 9)

def generate_random_character():
    return random.choice(string.ascii_letters)

def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
