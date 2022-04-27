from django.shortcuts import render

# Create your views here.
from django.template import loader


def main_cover(request):

    context = {
        'name': 'some_text',
    }
    return render(request, 'pages/startpage.html', context)
