import os

from django.core.mail import send_mail

import random

from dotenv import load_dotenv

load_dotenv()


def send(email):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    send_mail(subject='Ваш код подтвержения регистрации.',
              message=f'Ваш код OTP: {otp}',
              from_email=os.getenv('EMAIL_USER'),
              recipient_list=[email, ],
              fail_silently=False)
