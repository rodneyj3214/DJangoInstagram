# Create your views here.
from datetime import datetime

from django.http import HttpResponse

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE'
    }, {
        'name': 'Mont Blanc',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE'
    }, {
        'name': 'Mont Blanc',
        'user': 'Yesica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://i.picsum.photos/id/1036/200/200.jpg?hmac=Yb5E0WTltIYlUDPDqT-d0Llaaq0mJnwiCUtxx8RrtVE'
    |
]


def list_post(request):
    contact = []
    for post in posts:
        contact.append("""
        <p><strong>{name}</string></p>
        <p><small>{user} - <i>{timestamp}</i></small></p>
        <figure><img src="{picture}"></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(contact))
