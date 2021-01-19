from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html") 

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})    

def second(request):
    return HttpResponse('Test 2 page')  

def third(request):
    return HttpResponse('This is page test3')     
