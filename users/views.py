from django.shortcuts import render,redirect
from .models import UserProfile
from restaurant.models import Restaurant
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login,logout
from django.views.decorators.csrf import csrf_exempt

import requests#it is a python request object and its response is different from other response objects

from rest_framework.authtoken.models import Token #used to get a user from token

from django.contrib.auth.decorators import login_required


from django.contrib import messages #for displaying messages like save complete
from django.http import HttpResponse


base_url = '13.232.39.200:8000'


# Create your views here.
def login_view(request):
    if(request.method == 'POST'):
        try:
            parameters = {"username":request.POST['email'],"password":request.POST['pass']}
            r = requests.post('http://' +base_url+  '/auth/token/',data=parameters)
            print(r)
            if(r.status_code == 200):
                validate_email(request.POST['email'])
                request.session['token'] = r.json()['token']
                print(r.json())
                print('Navigating to nexxxt page')
                username = request.POST['email']
                password = request.POST['pass']
                #user = authenticate(request, username=username, password=password)#should authenticate first before logging in
                user = Token.objects.get(key=r.json()['token']).user
                print(user)
                if(user is not None):
                    print('Not None')
                    login(request,user)
                    messages.success(request, 'Successfully Logged In!')
                return redirect('home/')
                
            else:
                print('BAD RREquest')
        except ValidationError as e:
            print("bad email, details:",e)
            
    context = {}
    template = "Login/index.html"
    return render(request, template, context)

def signup_view(request):
    
    if (request.method == "POST"):
        restaurant = Restaurant.objects.create_restaurant(restaurant_name=request.POST['res_name'],address=request.POST['res_address'],)
        try:
            validate_email(request.POST['email'])
            if(request.POST['pass'] == request.POST['confirm_pass']):
                
                user = UserProfile.objects.create_user(email=request.POST['email'],name=request.POST['res_name'],password=request.POST['pass'])
                print('User Name is ' + user.name)
                messages.success(request, 'Your Account has been Created!')
                return redirect('/auth')
            else:
                print("Not Cool")
        except ValidationError as e:
            print("bad email, details:",e)

    context = {}
    template = "Login/signup.html"

    return render(request, template, context)





@login_required(login_url='/auth/')
def home_view(request):
    permission_classes = [IsAuthenticated] 
    template = "OrdersPage.html"
    response =  render(request,template,{})
    return response

def logout_view(request):
    try:
        logout(request)
        print("Logged Out")
        return redirect('/auth/')
    except:
        print("Error logging out")

def billing_view(request):
    template = "MainPage/billing.html"
    return render(request,template,{})

def menu_view(request):
    template = "MainPage/menu.html"
    return render(request,template,{})

def tables_view(request):
    template = "MainPage/tables.html"
    return render(request,template,{'range':range(0,10)})

def history_view(request):
    template = "MainPage/history.html"
    return render(request,template,{})

@csrf_exempt
def customer_signup(request):
    if(request.method == "POST"):
        try :
            validate_email(request.POST['email'])
            customer = UserProfile.objects.create_customer(email=request.POST['email'],name =request.POST['name'],password=request.POST['password'])
            print("Customer Is created" + customer.name)
            return HttpResponse("Your response")
        except ValidationError as e:
            print("Error occured")
            return


def customer_login(request):
    if(request.method == 'POST'):
        try:
            parameters = {"username":request.POST['email'],"password":request.POST['pass']}
            r = requests.post('http://' +base_url+  '/auth/token/',data=parameters)
            print(r)
            if(r.status_code == 200):
                validate_email(request.POST['email'])
                request.session['token'] = r.json()['token']
                print(r.json())
                print('Navigating to nexxxt page')
                username = request.POST['email']
                password = request.POST['pass']
                #user = authenticate(request, username=username, password=password)#should authenticate first before logging in
                user = Token.objects.get(key=r.json()['token']).user
                print(user)
                if(user is not None):
                    print('Not None')
                    login(request,user)
                    messages.success(request, 'Successfully Logged In!')
                return HttpResponse("Logged IN")
                
            else:
                print('BAD RREquest')
        except ValidationError as e:
            print("bad email, details:",e)
    return HttpResponse("Not Logged IN")
