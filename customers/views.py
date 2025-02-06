from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def sign_out(request):
    logout(request)
    return redirect('home')

def show_account(request):
    if request.POST and 'register' in request.POST: #if post request and register in request

        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            phoneno=request.POST.get('phoneno')

            #create user object
            user=User.objects.create(
                username=username,
                email=email
            )
            user.set_password(password)  # Hash the password before saving
            user.save()

            '''or
            #create user object using create_user
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            '''

            #create customer object using user object
            customer=Customer.objects.create(
                user=user,
                address=address,
                phone=phoneno
            )
            sucess_mesage = "User Registred Sucessfully"
            messages.success(request, sucess_mesage)
        
        except:
            error_message="Duplicate username or Invalid Credintials"
            messages.error(request, error_message)
    
    elif request.POST and 'login' in request.POST:
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:  # If user is found and credentials are correct
                login(request, user)
                success_message = "Login successful"
                messages.success(request, success_message)
            
            else:
                error_message = "Invalid credentials"
                messages.error(request, error_message)
        
        except Exception as e:
            error_message = "An error occurred during login: " + str(e)
            messages.error(request, error_message)

    return render(request, 'account.html')