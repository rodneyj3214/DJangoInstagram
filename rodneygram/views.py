from datetime import datetime

from django.http import HttpResponse


def hello_word(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('The current server time is {now}'.format(now=str(now)))


def hi(request):
    print(request)
    import pdb; pdb.set_trace()
    return HttpResponse('Hi')
