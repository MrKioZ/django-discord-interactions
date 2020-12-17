from .variables import *
from .models import GlobalCommandStorage

class UnExpectedReturn(Exception):
    pass

commands_methods = {}

def GlobalCommand(func):

    commands_methods.update({func.__name__: func})
    try:
        command = GlobalCommandStorage.objects.get(name=func.__name__)
    except GlobalCommandStorage.DoesNotExist:
        GlobalCommandStorage.objects.create(name=func.__name__, description="foo bar")

    def decorated(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if not isinstance(result, GlobalCommand):
                raise UnExpectedReturn('Expected to return GlobalCommand object')
        finally:
            pass        

    return decorated

@GlobalCommand
def welcome(data):
    print(dict(data))

    response = {
        "data": {
            "content": "Hello World"
        }
    }
    return InteractionResponse(**response)