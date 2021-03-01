"""Posts views"""

# Django
from django.http import HttpResponse
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://i.picsum.photos/id/515/200/300.jpg?grayscale&hmac=H7HhCstLQK3d17xj1gO85bAVCtKXyMM5BiMp_f2gDMs'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/866/200/300.jpg?hmac=rcadCENKh4rD6MAp6V_ma-AyWv641M4iiOpe1RyFHeI'
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://i.picsum.photos/id/862/200/300.jpg?grayscale&hmac=h762kHJSmkzXR2YkW_GfjOaiPB3qoz4zVBuifFLk9-c'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/790/200/300.jpg?grayscale&hmac=9e3GQvah8nBLGGhLdcbagvakf0_kb-iEzBYT-1gfs1Q'
    },
    {
        'title': 'nuevo auditorio',
        'user': {
            'name': 'Publico',
            'picture': 'https://i.picsum.photos/id/444/200/300.jpg?grayscale&hmac=c7xahcRpOC2purUCsstI5qdpHRVnrtPm690m_9PQ-Ko'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U'
    },

]


def list_posts(request):
    """Lists existing posts"""

    return render(request, 'posts/feed.html', {'posts': posts})