from django.shortcuts import render
from .models import Book_description
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import re
from unicodedata import normalize as norm

# Create your views here.

SEARCH_RESULTS = {'results':[]}

READ_MORE_RESULTS = {'data':[]}

def upload_func(file,name_file):
    with open('APLICATION_LIBRARY_PRECISA/static/{}'.format(name_file), 'wb+') as f:
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



    book_name = str(data['book_name'])

    book_name = norm('NFKD', book_name).encode('ascii', 'ignore').decode()

    book_name = re.sub(r'[^a-zA-Z0-9]',' ',book_name)

    book_name = re.sub(r'\s+',' ',book_name)

    

    


    author = str(data['author'])

    author = norm('NFKD', author).encode('ascii', 'ignore').decode()

    author = re.sub(r'[^a-zA-Z0-9]',' ',author)

    author = re.sub(r'\s+',' ',author)

    

    url_image = 'images/'+book_name+"_"+author+"_"+str(data['volume'])+"_"+str(data['version'])+"_"+str(data['category'])+".jpg"

    
    upload_func(picture,url_image)


    Book_description.objects.create(book_name=data['book_name'],
                                    synopsis=data['synopsis'],
                                    author = data['author'],
                                    volume=data['volume'],
                                    version=data['version'],
                                    category=data['category'],
                                    url_image = url_image)


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


    data = json.loads(request.POST.get('request'))

    picture = request.FILES.get('file')

    
    upload_func(picture)

    return JsonResponse({"teste":"succeed"})



@csrf_exempt
def index(request):

    books = Book_description.objects.all()


    data = {

        'data_book': books
    }

    return render(request,"index.html",data)

@csrf_exempt
def read_more(request):

    data_read_more = READ_MORE_RESULTS['data'] 

    books = Book_description.objects.all()


    data = {

        'data_read_more': data_read_more,
        'data_book': books
    }

    return render(request,"read_more.html",data)

@csrf_exempt
def search_results(request):

    #books =  Book_description.objects.get(book_name="harry")

    #books = Book_description.objects.filter(book_name=SEARCH_RESULTS['results'])

    books = Book_description.objects.all()


    try:


        search_str_modified = SEARCH_RESULTS['results'].lower()


        search_str_modified = search_str_modified.replace(" ","")


    except:

        search_str_modified = ""

    list_books_search = []


    for iterator_book in books:

        str_base_book = iterator_book.book_name

        str_base_book = str_base_book.lower()

        str_base_book = str_base_book.replace(" ","")


        if str_base_book[0:len(search_str_modified)]==search_str_modified:



            list_books_search.append({"book_name":iterator_book.book_name,
            "author":iterator_book.author,
            "url":iterator_book.url_image,"volume":iterator_book.volume,"version":iterator_book.version,"synopsis":iterator_book.synopsis})




    data = {

        'data_book': books,
        'data_book_modified': list_books_search,
        'search':SEARCH_RESULTS['results']
    }



    return render(request,"search_products.html",data)


    
@csrf_exempt
def delete_all(request):

  Book_description.objects.all().delete()

  return JsonResponse({"response":"all rows deleted"})


@csrf_exempt
def results(request):


    data = json.loads(json.dumps(request.POST))


    SEARCH_RESULTS['results'] = data['name_book']

    return JsonResponse({"response":"search completed"})



@csrf_exempt
def persist_read_more(request):


    data = json.loads(json.dumps(request.POST))

    #data = json.loads(request.POST.get('info'))


    READ_MORE_RESULTS['data'] = data

    return JsonResponse({"response":"read more completed"})