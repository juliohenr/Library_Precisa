from django.shortcuts import render
from .models import Book_description
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def get_books(request):

    books = Book_description.objects.all()

    print("\n")
    print(list(books.values()))
    print("\n")

    return JsonResponse({"teste":1})

def index(request):

    books = Book_description.objects.all()

    print("\n")
    print(list(books.values()))
    print("\n")

    return JsonResponse({"teste":2})



