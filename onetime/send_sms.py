import serial
import time

def send_sms(phone_number, message):
    ser = serial.Serial('COM4', baudrate=9600, timeout=5)  # Adjust the COM port as per your connection

    ser.write(b'AT\r')
    time.sleep(0.5)
    ser.write(b'AT+CMGF=1\r')  # Set SMS to text mode
    time.sleep(0.5)
    
    ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
    time.sleep(0.5)
    ser.write(f'{message}\x1A'.encode())  # \x1A is the Ctrl+Z character to send the SMS
    time.sleep(0.5)
    
    response = ser.read(ser.inWaiting()).decode()
    ser.close()
    return response

if __name__ == "__main__":
    phone_number = "1234567890"  # Replace with the recipient's phone number
    message = "Your OTP code is 123456"
    response = send_sms(phone_number, message)
    print(response)
