import os

class Config(object):
    MKAD_CENTER = [37.612, 55.71]
    MKAD_COORDINATES = [(37.329, 37.895),(55.503, 55.917)]
    API_KEY = "8c53cc8d-2f29-491d-9fc5-3e4f4ea0dc67"
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-very-secret-key-123789456'
    ERROR_MESSAGE = "Address not found or wrong address"
    TARGET_IN_MKAD_MESSAGE = "Location is inside of Moscow Ring Road."
    ADDR_EMPTY = "Address can't be empty."