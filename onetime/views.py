from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import pyotp
from django.conf import settings
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from django.urls import reverse
import json


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.phone_number  # Use phone number as username
            user.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)
                return redirect(reverse('login'))  # Redirect to the login page
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
                                                               
def login(request): 
    error_message = None
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        user = CustomUser.objects.filter(phone_number=phone_number).first()
        if user is not None:
            request.session['phone_number'] = phone_number
            send_otp(request, user.phone_number)  # Send OTP to phone number
            return redirect('otp')
        else:
            error_message = 'Invalid phone number'
    return render(request, 'login.html', {'error_message': error_message})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.conf import settings
import pyotp
from datetime import datetime, timedelta

def otp(request):
    error_message = None

    try:
        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_until']
    except KeyError:
        error_message = 'Session data not found. Please login again.'
        return render(request, 'otp.html', {'error_message': error_message})

    if request.method == 'POST':
        otp = request.POST.get('otp')  # Use .get() to safely access POST data
        phone_number = request.session.get('phone_number')

        if otp_secret_key and otp_valid_until:
            valid_until = datetime.fromisoformat(otp_valid_until)

            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)
                if totp.verify(otp):
                    user = get_object_or_404(CustomUser, phone_number=phone_number)
                    auth_login(request, user)

                    # Clean up the session data
                    for key in ['otp_secret_key', 'otp_valid_until', 'phone_number']:
                        if key in request.session:
                            del request.session[key]

                    return redirect('announce.html')  # Use the name defined in urlpatterns
                else:
                    error_message = 'Invalid OTP'
            else:
                error_message = 'OTP has expired'
        else:
            error_message = 'Something went wrong'

    return render(request, 'otp.html', {'error_message': error_message})



@login_required
def main(request):
    if 'phone_number' in request.session:
        del request.session['phone_number']
    return render(request, 'main.html', {})

def logout(request):
    auth_logout(request)
    return redirect('login')

def send_otp(request, phone_number):
    # Generate a random OTP secret key
    otp_secret_key = pyotp.random_base32()

    # Store the OTP secret key and valid until time in the session
    request.session['otp_secret_key'] = otp_secret_key
    request.session['otp_valid_until'] = (datetime.now() + timedelta(minutes=settings.OTP_EXPIRY_DURATION)).isoformat()

    # Generate the OTP using the TOTP algorithm
    totp = pyotp.TOTP(otp_secret_key, interval=60)
    otp = totp.now()

    # Here you would send the OTP to the user's phone number
    # For demonstration, we'll just print it to the console
    print(f"Sending OTP {otp} to phone number {phone_number}")
 
def json_ot(request):
    data=list(CustomUser.objects.values())
    return JsonResponse(data,safe=False)  
