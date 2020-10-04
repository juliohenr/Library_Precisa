from django.shortcuts import render
from .models import Book_description
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def upload_func(file,name_file):
    with open('./UPLOAD/{}'.format(name_file), 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)

@csrf_exempt
def get_books(request):

    books = Book_description.objects.all()


    return JsonResponse({"data":list(books.values())})


@csrf_exempt
def add_books(request):


    data = json.loads(request.POST.get('request'))

    picture = request.FILES.get('file')

    name_file = str(data['book_name'])+"_"+str(data['volume'])+"_"+str(data['version'])+"_"+str(data['category'])+".jpg"

    
    upload_func(picture,name_file)


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




@csrf_exempt
def test_binary(request):

    #data = json.loads(request.body)

    #print(data)

    print("\n")
    print("\n")
    #print(data)
    data = json.loads(request.POST.get('request'))
    print(data)
    print("\n")
    print(request.FILES.get('file'))
    print("\n")
    print(type(request.FILES.get('file')))
    print("\n")
    picture = request.FILES.get('file')

    
    upload_func(picture)

    return JsonResponse({"teste":"succeed"})




def index(request):

    books = Book_description.objects.all()


    return JsonResponse({"teste":2})



