from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Books

def homepage(request):
    return render(request, "index.html") 

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})    

def second(request):
    return HttpResponse('Test 2 page')  

def third(request):
    book_list = Books.objects.all()
    return render(request, "books.html", {"book_list": book_list})     

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
     todo = ToDo.objects.get(id=id)
     todo.delete()
     return redirect(test) 


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)      


def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)         

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = Books(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)   
    book.save()
    return redirect(third) 

def delete_book(request, id):
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(third)

def select_book(request, id):
    book = Books.objects.get(id=id)
    book.is_favorites = True
    book.save()
    return redirect(third)


def BooksDetail(request, id):
    book = Books.objects.get(id=id)
    book.save()
    title = Books.objects.all()
    return render(request, "books_detail.html", {'title': title})
    #return HttpResponse(render(request, "books_detail.html"))