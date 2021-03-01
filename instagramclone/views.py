"""File views to instagramclone"""

# Django
from django.http import HttpResponse
import json
# Utilities
from datetime import datetime


def hello_world(request):
    """retorna un saludo"""
    now = datetime.now()
    # import pdb; pdb.set_trace()
    return HttpResponse('Oh, hi! the Current server time is {now}'.format(now=str(now)))


def sort_integers(request):
    """return a Json with sorted integers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted susccesfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def hi(request, name, age):
    """check parameter age > 12 year old"""
    if age < 12:
        message = "Sorry, {} you are so young".format(name)
    else:
        message = "Hello {} welcome to instagramclone".format(name)
    return HttpResponse(message)
