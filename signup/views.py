from django.shortcuts import render 
from django.http import HttpResponse 
from .db_connect  import insert,verify

def home(request): 
    print(request.POST)
    return render(request, 'index.html') 

def login(request): 
    print("login hit")  
    print(request.POST)   
    request.POST = request.POST.copy() 
    data = request.POST 
    status = verify(data)
    return render(request, 'result.html', {'status' : status}) 

def signup(request):  
    print("Sign up hit")
    print(request.POST)  
    data_recevied = request.POST
    return render(request,'signup.html')   

def register(request):  
    print("register hit") 
    request.POST = request.POST.copy()
    data_recevied = request.POST  
    del data_recevied['csrfmiddlewaretoken'] 
    data_recevied = data_recevied.dict()
    status = insert(data_recevied)
    print(status) 
    if status == False: 
        return render(request,'signup_fail.html')  
    else: 
        return render(request,'index.html')

      
