import os

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from askdjango import settings


def mysum(request, numbers):
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse('안녕하세요 {}. {} 살이시네요'.format(name, age))

def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>Hi this is Bligh</h1>
    <p>{name}</p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list.html', {'name':name})


def post_list3(request):
    return JsonResponse({
        'message' : '안녕 파이썬 장고',
        'items' : ['파이썬', '장고', '애저'],
    }, json_dumps_params={'ensure_ascii':False})


def excel_download(request):
    #filepath = '/Users/Bligh_Park/PycharmProjects/askdjango/mostrecent.csv'
    filepath = os.path.join(settings.BASE_DIR, 'mostrecent.csv')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')

        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
