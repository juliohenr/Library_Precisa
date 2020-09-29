from django.shortcuts import render
from .models import Book_description
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def get_books(request):

    books = Book_description.objects.all()


    return JsonResponse({"data":list(books.values())})


@csrf_exempt
def add_books(request):

    books = Book_description.objects.all()


    data = json.loads(request.body)


    Book_description.objects.create(book_name=data['book_name'],
                                    synopsis=data['synopsis'],
                                    author = data['author'],
                                    volume=data['volume'],
                                    version=data['version'],
                                    category=data['category'])


    return JsonResponse({"response":"row added"})


@csrf_exempt
def delete_books(request):

    books = Book_description.objects.all()


    data = json.loads(request.body)


    Book_description.objects.filter(id=data['id']).delete()


    return JsonResponse({"response":"row deleted"})


@csrf_exempt
def update_books(request):

    books = Book_description.objects.all()


    data = json.loads(request.body)

    print(data)


    book_obj = Book_description.objects.get(id=data['id'])
    

    if 'book_name' in data.keys():

        book_obj.book_name = data['book_name']

    if 'synopsis' in data.keys():

        book_obj.synopsis = data['synopsis']


    if 'author' in data.keys():

        book_obj.author = data['author']


    if 'volume' in data.keys():

        book_obj.volume = data['volume']

    if 'version' in data.keys():

        book_obj.version = data['version']

    if 'category' in data.keys():

        book_obj.category = data['category']


    book_obj.save()


    return JsonResponse({"response":"row updated"})











def index(request):

    books = Book_description.objects.all()


    return JsonResponse({"teste":2})



