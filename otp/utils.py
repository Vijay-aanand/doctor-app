import random
from datetime import datetime, timedelta
from django.conf import settings


def generate_otp(length=6):
    # Generate random OTP of specified length
    otp = ''.join(random.choices('0123456789', k=length))
    return otp

def send_otp(request, phone_number):
    # Generate OTP
    otp = generate_otp()

    # Save OTP and its expiration time in session
    request.session['otp'] = otp
    request.session['otp_valid_until'] = (datetime.now() + timedelta(minutes=settings.OTP_EXPIRY_DURATION)).isoformat()

    # For demonstration, print OTP instead of sending SMS
    print(f"Your OTP for login is: {otp}")

    return otp

def verify_otp(request, otp, phone_number):
    # Retrieve OTP and its expiration time from session
    saved_otp = request.session.get('otp')
    otp_valid_until = request.session.get('otp_valid_until')

    # Check if OTP is valid and not expired
    if saved_otp == otp and datetime.now() < datetime.fromisoformat(otp_valid_until):
        return True
    else:
        return False
